import random
import sys


def create_shuffled_deck():
    suites = ["Clubs", "Diamonds", "Spades", "Hearts"]
    list_of_cards = []
    for j in range(0, 4):
        for i in range(0, 13):
            if (i + 1) % 15 > 10:  # deal with face values
                list_of_cards.insert(i, [str(10), suites[j]])
            else:
                list_of_cards.insert(i, [str((i + 1) % 15), suites[j]])
    return random.sample(list_of_cards, len(list_of_cards))


def calculate_sum(cur_hand):
    p_sum = 0
    for card in cur_hand:
        if int(card[0]) == 1:
            p_sum = p_sum + ace_value()
        else:
            p_sum = p_sum + int(card[0])
    return p_sum


def calculate_house_sum(cur_hand, cur_sum):
    h_sum = 0
    for card in cur_hand:
        if int(card[0]) == 1:  # if the house has an Ace, can be 1 or 11 based on the rest of the cards
            if cur_sum + 11 <= 21:
                h_sum = cur_sum + 11
            else:
                h_sum = cur_sum + 1
        else:
            h_sum = h_sum + int(card[0])
    return h_sum


def house_play(cur_hand, p_sum, deck, i):
    """depending on the players sum and the dealer's current sum, the house hits or stands"""
    house_sum = 0
    house_sum = int(calculate_house_sum(cur_hand, house_sum))
    if p_sum == 21:
        while house_sum < 21:
            cur_hand.append(deck[i])
            i += 1
            house_sum = calculate_house_sum(cur_hand, house_sum)
    elif house_sum > p_sum:
        print("House sum: " + str(house_sum) + ". Your sum: " + str(p_sum))
        print("You lose")
        return
    else:
        while house_sum < 16 and house_sum < p_sum:
            cur_hand.append(deck[i])
            i += 1
            house_sum = calculate_house_sum(cur_hand, house_sum)
    if house_sum == p_sum:
        print("House sum: " + str(house_sum) + ". Your sum: " + str(p_sum))
        print("You Tied with House")
        return
    if house_sum < p_sum or (house_sum != 21 and p_sum == 21) or house_sum > 21:
        print("House sum: " + str(house_sum) + ". Your sum: " + str(p_sum))
        print("You win")
        return
    else:
        print("House sum: " + str(house_sum) + ". Your sum: " + str(p_sum))
        print("You lose")


def print_current_hand(player_hand):
    """prints the current hand """
    print("Your current hand is:")
    for cards in player_hand:
        if int(cards[0]) == 1:
            print("Ace of " + cards[1])
        else:
            print(str(cards[0]) + " of " + str(cards[1]))


def ace_value():
    """Gives player the option to choose an 1 or 11 for their ace value"""
    value = int(input("You have an Ace. Would you like to choose 1 or 11 as the value? "))
    if value == 1 or value == 11:
        return int(value)
    else:
        while (int(value) != 1) and (int(value) != 11):
            value = int(input("Invalid value. Try again: "))
    return int(value)


def play_game():
    """intializes the hands of the player and the house, and then allows player to play until they stand
    or bust and then the house plays"""
    deck = create_shuffled_deck()

    player_hand = [deck[0], deck[1]]
    print_current_hand(player_hand)
    house_hand = [deck[2], deck[3]]
    player_sum = calculate_sum(player_hand)
    i = 4
    result = True
    if int(house_hand[0][0]) == 1:
        print("The dealer's face up card is an Ace")
    else:
        print("The dealer's face up card is a " + house_hand[0][0] + " of " + house_hand[0][1])
    choice = input("Would you like to hit or stand?(h/s) ")
    while choice != "s":
        if choice == "h":
            player_hand.append(deck[i])
            cur_card = deck[i]
            if int(cur_card[0]) == 1:
                print("You drew a Ace of " + cur_card[1])
            else:
                print("You drew a " + cur_card[0] + " of " + cur_card[1])
            i += 1
            if int(cur_card[0]) == 1:
                player_sum = player_sum + ace_value()
            else:
                player_sum = player_sum + int(cur_card[0])
            print("Your current sum is " + str(player_sum))
            if player_sum > 21:
                print("House wins. Your sum exceeded 21")
                sys.exit()
            else:
                choice = input("Would you like to hit or stand?(h/s) ")

    house_play(house_hand, player_sum, deck, i)
    sys.exit()


play_game()
