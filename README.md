---

# Coin Toss Game

Welcome to the Coin Toss Game! This is a simple, interactive Python game where the user can predict the outcome of a coin flip. The game will randomly generate either "Head" or "Tail" and compare it with the user's prediction. It's a fun way to test your luck! 🎲

---

## Features

- **Interactive Gameplay**: The game asks the player to predict whether the coin will land on heads or tails.
- **Random Coin Toss**: The game simulates a coin toss using Python's `random.choice()` to choose randomly between "Head" and "Tail".
- **Personalized Experience**: The game greets the user by name and provides feedback on whether the prediction was correct.
- **Input Validation**: Ensures the user provides a valid prediction ("Head" or "Tail").

---

## Requirements

To run this game, you'll need to have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

This script uses the built-in `random` module, which is available in standard Python installations, so no additional dependencies are required.

---

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/AyushTIW30/Coin_Toss_Game/blob/main/Coin_Toss.py
    ```

2. Navigate to the project directory:
    ```bash
    cd Coin_Toss_Game
    ```

3. Ensure Python is installed. You can check this by running:
    ```bash
    python --version
    ```
    Or, if you're using Python 3 specifically:
    ```bash
    python3 --version
    ```

---

## How to Play

1. Run the script by executing the following command in your terminal:
    ```bash
    python coin_toss_game.py
    ```

2. The game will prompt you to enter your name.
   
3. After entering your name, you’ll be asked to predict whether the coin will land on "Head" or "Tail".

4. The coin will be tossed, and the outcome will be shown. You’ll receive a message indicating whether your prediction was correct or not.

---

## Example Gameplay

```bash
----------------------------------------------
      Welcome to the Coin Toss Game!         
  ----------------------------------------  
In this game, you'll flip a coin and predict
whether it will land on heads or tails. Let's
see if you're lucky today! 😄

----------------------------------------------
Please enter your name: Alice

Hello, Alice! Let's get started!

Predict the outcome! Will it be 'Head' or 'Tail'? Head

----------------------------------------------
           The coin is tossed...             
----------------------------------------------

The coin landed on: Tail
Sorry, Alice. Better luck next time! 😔
```

---

## Code Structure

- **`display_welcome_message()`**: Displays an introductory message explaining the game.
- **`get_user_name()`**: Prompts the user to enter their name and returns it for personalization.
- **`coin_toss()`**: Simulates the coin toss using Python's `random.choice()` method.
- **`get_user_prediction()`**: Asks the user to predict the outcome of the coin toss and validates the input.
- **`display_results()`**: Compares the user's prediction with the toss result and provides feedback.
- **`run_game()`**: Main function that ties everything together and runs the game.

---

## Contributing

Contributions are welcome! If you'd like to improve the game or add new features, feel free to fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions or suggestions, feel free to open an issue on GitHub or contact me directly.

---

## Acknowledgements

- Thanks to Python’s random module for helping us simulate the coin toss.
- Special thanks to anyone who takes the time to play this game and provide feedback.

---

