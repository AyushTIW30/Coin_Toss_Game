import random

# Function to display a welcome message and explain the game
def display_welcome_message():
    print("\n----------------------------------------------")
    print("      Welcome to the Coin Toss Game!         ")
    print("  ----------------------------------------  ")
    print("In this game, you'll flip a coin and predict")
    print("whether it will land on heads or tails. Let's")
    print("see if you're lucky today! 😄\n")
    print("----------------------------------------------\n")

# Function to get user's name and display personalized greeting
def get_user_name():
    name = input("Please enter your name: ")
    print(f"\nHello, {name}! Let's get started!\n")
    return name

# Function to perform the coin toss
def coin_toss():
    toss_result = random.choice(["Head", "Tail"])
    return toss_result

# Function to ask the user to predict the coin toss outcome
def get_user_prediction():
    while True:
        prediction = input("Predict the outcome! Will it be 'Head' or 'Tail'? ").capitalize()
        if prediction in ["Head", "Tail"]:
            return prediction
        else:
            print("Invalid input! Please enter either 'Head' or 'Tail'.\n")

# Function to display the result of the coin toss and compare with the user's prediction
def display_results(prediction, toss_result, name):
    print("\n----------------------------------------------")
    print("           The coin is tossed...             ")
    print("----------------------------------------------\n")
    print(f"The coin landed on: {toss_result}")

    if prediction == toss_result:
        print(f"Congratulations, {name}! Your prediction was correct! 🎉\n")
    else:
        print(f"Sorry, {name}. Better luck next time! 😔\n")

# Main function to run the game
def run_game():
    display_welcome_message()

    name = get_user_name()  # Get user's name

    user_prediction = get_user_prediction()  # Get user's prediction

    toss_result = coin_toss()  # Perform the coin toss

    display_results(user_prediction, toss_result, name)  # Display the result

# Run the game
if __name__ == "__main__":
    run_game()
