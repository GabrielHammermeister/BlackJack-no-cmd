from BlackJack import Deck, Card, Player, suits, ranks, values
import os


def count_value(card: Card, player: Player):
    player.points += card.value

def display_board(machine: Player, human: Player):
    os.system('cls' if os.name == 'nt' else 'clear')

    machine_cards = len(machine.hand)
    human_cards = len(human.hand)
    print("\n-------------------------------------------------")
    for i in range(machine_cards):
        if i == 0:
            print("   OCULT - ", end = '')
        elif i == machine_cards - 1:
            print(machine.hand[i] , "\n")
        else:
            print(machine.hand[i], " - ", end='')
    print("   ", end = '')
    for i in range(human_cards):
        if i == human_cards - 1:
            print(human.hand[i])
        else:
            print(human.hand[i], " - ", end = '')
    print("-------------------------------------------------")
    print("points: ", human.points, "\n")

def first_draw(main_deck, human_player, machine):
    human_player.points = 0
    machine.points = 0

    for i in range(2):
        card = main_deck.draw_card()
        score = card.value
        human_player.hand.append(card)
        human_player.points += score

        card = main_deck.draw_card()
        score = card.value
        machine.hand.append(card)
        machine.points += score

def hit(player: Player, deck: Deck):
    try:
        card = deck.draw_card()
        score = card.value
        if card.rank == 'Ace' and player.name == "Human Player":
            score = int(input("You got an ACE!\nChoose 1 or 11: "))

        player.hand.append(card)
        player.points += score
    except IndexError:
        print("No cards left in the deck.")

if __name__ == '__main__':


    human_player = Player("Human Player")
    machine = Player("Computer Dealer")

    h = 0
    m = 0
    game_on = True
    while game_on:

        human_player.hand = []
        machine.hand = []

        # SHUFFLING AND RECEIVING THE FIRST HAND
        main_deck = Deck()
        main_deck.shuffle_cards()
        first_draw(main_deck, human_player, machine)


        # RECEIVING THE FIRST BET
        if human_player.account == 0:
            print("You have no Credit to BET!\n--- GAME OVER ---")
            break

        bet = float(input("Put a BET in the board: "))
        while human_player.account - bet < 0:
            bet = float(input("The BET is to high!\nTry again: "))
        human_player.account -= bet

        # HUMAN PLAYER TURN
        while True:

            display_board(machine, human_player)
            answer = int(input("1 - Hit (receive another card)\n2 - Stay (Stop receiving cards)\n\n>>> "))

            if answer == 1:
                hit(human_player, main_deck)
                h = human_player.points

                if h >= 21:
                    break
                else:
                    has_hit = False
            else:
                break

        if h < 21:
            # MACHINE DEALER TURN
            while True:
                hit(machine, main_deck)
                m = machine.points
                if h < m <= 21:     # MACHINE BEAT HUMAN
                    display_board(machine, human_player)
                    print("Human Player LOST THE ROUND !!!")
                    break
                elif m > 21:    # MACHINE BUSTS
                    display_board(machine, human_player)
                    print("Human Player WON THE ROUND !!!")
                    human_player.account += bet*2
                    break

        elif h == 21:   # HUMAN BEAT MACHINE
            display_board(machine, human_player)
            print("Human Player WON THE ROUND !!!")
            human_player.account += bet*2
        else:
            display_board(machine, human_player)
            print("Human Player LOST THE ROUND !!!")

        answer = int(input("\nDo you want to Leave?\n[1] Yes\n[2] No\n\n>>> "))
        if answer == 1:
            print(human_player, "\nEnd of the Game!")
            game_on = False
        else:
            print(human_player, end = '\n\n')
            continue
else:
    print("BlackJackMain has been imported...")
