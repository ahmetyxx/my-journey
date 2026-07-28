import random as r
import art
import game_data



def game():
    is_game_ended=False
    first=True
    current_score=0

    a=r.choice(game_data.data)
    b=a

    while not is_game_ended:
        print(art.logo)
        if not first:
            print(f"You're right! Current score: {current_score}")
        while b == a:
            b = r.choice(game_data.data)

        print(f"")


        print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
        print(art.vs)
        print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")

        follower_A = a["follower_count"]
        follower_B = b["follower_count"]

        bigger=""
        if follower_A>follower_B:
            bigger="a"
        elif follower_A<follower_B:
            bigger="b"


        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()

            if guess in ("a", "b"):
                break

            print("Please enter only 'A' or 'B'.")

        if guess == bigger:
            a=b
            first=False
            current_score+=1
            print("\n"*20)
            b=r.choice(game_data.data)
        elif guess !=bigger:
            is_game_ended=True
            print("\n" * 20)
            print(f"Sorry, that's wrong. Final score: {current_score}")
game()







#TODO: if user's guess is wrong make is_game_ended true and clear the page
# display the logo and Sorry, that's wrong. Final score: {current_score}

