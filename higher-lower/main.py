from art import logo, vs
from game_data import data
import random
import os

def clear_terminal():
    """For clearing the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def provide_option(option, dict):
    """Takes a dictionary and displays the output in required format"""
    """ {
            'name': 'Instagram',
            'follower_count': 346,
            'description': 'Social media platform',
            'country': 'United States'
        } """
    if option == "A":
        print(f"Compare A: {dict['name']}, {dict['description']}, from {dict['country']}")
    else:
        print(f"Against B: {dict['name']}, {dict['description']}, from {dict['country']}")

score = 0 
choice_dict = {}
is_answer_correct = True
while is_answer_correct:
    print(logo)
    if score != 0:
        print(f"You're right! Current Score: {score}")

    #Will receive a random dictionary from data
    choice_dict["A"] = random.choice(data)
    choice_dict["B" ] = random.choice(data)
    
    provide_option("A", choice_dict["A"])
    print(vs)
    provide_option("B", choice_dict["B"])
    
    #Taking the answer from the user
    user_guess = input("Who has more followers? Type 'A' or 'B':  ")
    if user_guess == "A":
        user_guess_followers = choice_dict["A"]['follower_count']
        opponent_followers = choice_dict["B"]['follower_count']
    else:
        user_guess_followers = choice_dict["B"]['follower_count']
        opponent_followers = choice_dict["A"]['follower_count']       

    #Checking whether the guess is correct or not
    if user_guess_followers > opponent_followers:
        score += 1
    else:
        is_answer_correct = False
    clear_terminal()


print(logo)
print(f"Sorry, that's wrong. Final score: {score}")

