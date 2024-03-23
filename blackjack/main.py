from art import logo
import random
print(logo)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_set):
    """Take a list of cards and return the score calculated from cards"""
    total_value = 0
    for card in card_set:
        total_value += card 
    
    #Cheking for blackjack
    if total_value == 21 and len(card_set) == 2:
        return 0
    
    #Handling ace
    if 11 in card_set and total_value > 21:
        card_set.remove(11)
        card_set.append(1)
        total_value -= 10
    return total_value

def compare(user_score , computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lost! opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You won!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


player_set = []
dealer_set = []
is_game_over = False


#Initializing the game
#Giving 2 cards to the player and one card to the dealer
for _ in range(2):
    player_set.append(deal_card())
    dealer_set.append(deal_card())

while not is_game_over:
    player_score = calculate_score(player_set)
    computer_score = calculate_score(dealer_set)
    print(f"Your cards: {player_set}, current score: {player_score}")
    print(f"Computer's first card {dealer_set[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            player_set.append(deal_card())
        else:
            is_game_over = True


# The computer should keep drawing the card as long as it is less than 17
while computer_score != 0 and computer_score < 17:
    dealer_set.append(deal_card())
    computer_score = calculate_score(dealer_set)

print(f"Your final hand: {player_set}, final score: {player_score}")
print(f"Computer's final hand: {dealer_set}, final score: {computer_score}")
print(compare(calculate_score(player_set), calculate_score(dealer_set)))


