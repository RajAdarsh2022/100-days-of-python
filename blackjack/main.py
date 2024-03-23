from art import logo
import random
print(logo)


def find_sum(card_set):
    total_value = 0
    for card in card_set:
        total_value += card 
    return total_value

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player_set = []
dealer_set = []


#Initializing the game
#Giving 2 cards to the player and one card to the dealer
player_set.append(random.choice(cards))
dealer_set.append(random.choice(cards))
flag = "y"



while flag == "y":
    player_set.append(random.choice(cards))
    print(f"Your cards: {player_set}, current score: {find_sum(player_set)}")
    print(f"Computer's first card {dealer_set[0]}")
    if find_sum(player_set)  > 21:
        break
    flag = input("Type 'y' to get another card, type 'n' to pass: ")

while find_sum(dealer_set) < 17:
    dealer_set.append(random.choice(cards))


print(f"Your final hand: {player_set}, final score: {find_sum(player_set)}")
print(f"Computer's final hand: {dealer_set}, final score: {find_sum(dealer_set)}")
if find_sum(player_set) > 21:
    print("You went over. You lose!")
elif find_sum(dealer_set) > 21:
    print("Computer went over. You won!")
else:
    if find_sum(player_set) > find_sum(dealer_set):
        print("You scored more. You won!")
    elif find_sum(player_set) == find_sum(dealer_set):
        print("The match resulted in a draw.")
    else:
        print("Computer scored more. You lose!")
