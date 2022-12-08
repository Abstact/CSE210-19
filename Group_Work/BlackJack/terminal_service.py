# Some of the intrsutions are taken from (https://1883magazine.com/how-to-play-blackjack-online-step-by-step-guide/)

from termcolor import colored
import random

class Terminal():
    """
        Class that controls the terminal service
    """
    def __init__(self) -> None:
        pass
        

    def intro():
        """
            Shows a welcome message
        """
        print("Welcome to Blackjack!")

        def ask():
            """
                Asks the user if they would want to read the instructions.
            """
            read_instructions = input(f"Do you want to read the instructions(Y/N)?\n\t→ ")
            if read_instructions.upper() == "Y":
                print("\nHow to Play:")
                print("\n→ You get 2 cards dealt to you")
                print("→ Decide when you want to 'HIT'\n\t-This increases the value of your hand\n\t-If you cross 21 and go bust, you lose your money")
                print("\t-You have to make sure that you have healthy hand\n\t and that if it cross values of 16 or 17, you should \n\t decide if you are willing to take a risk")
                print("→ Decide when you want to 'STAND'\n\t-When you are satisfied with your hand, choose to STAND")
                print("→ The Outcome\n\t-You WIN if the value of the cards in your \n\t hand are higher than the dealers or is equal to 21")
                print("\n\t- If the value of your hand is lower than the \n\t dealers or cross 21, you LOSE")

            elif read_instructions.upper() == "N":
                print("I guess you're ready. Let's Go!")

            else:
                print("Please enter either Y or N\n\t→ ")
                ask()
        ask()

    def player_win():
        """
            Display random player won messages
        """
        winning_statements = ["Heh, I knew you'd win!", 
                            "Didn't doubt you a bit", 
                            "Wow, you're so lucky!", 
                            "Looks like luck's on your side today!", 
                            "You won!"]

        print(random.choice(winning_statements))

    def dealer_win():
        """
            Display random player lost messages
        """
        losing_statements = ["Better luck next time!",
                            "Too bad",
                            "You can do better!",
                            "You lost"]

        print(random.choice(losing_statements))

    def tie():
        """
            Display random tie messages
        """
        tie_statements = ["It's a tie!",
                        "You just tied with the dealer!",
                        "It's a draw!",
                        "That was tense, yet a draw"]
        
        print(random.choice(tie_statements))

    def score(player_score, dealer_score):
        """
            Displays both scores

            Args:
                player_score
                dealer_score
        """
        print(colored(f"Your score: {player_score}", "blue"))
        print(colored(f"Dealer's Score: {dealer_score}"), "red")

    def goodbye():
        """
            Goodbye message
        """
        print("Thank you for playing Blackjack with us!\nSee ya again next time!")

    def show_card(card_number, card_color):
        """
            Displays the card in the terminal.

            Arg(s):
                card_number: Gets the value of the card to display
                card_color: Identify whether it is...
                                - Hearts: Red
                                - Clubs: Blue
                                - Spades: Green
                                - Diamonds: Yellow

            Example: 
                show_card(A, "red")
                show_card(10, "blue")
        """
        if len(str(card_number)) == 1:
            card = f"_____\n|   |\n| {card_number} |\n|___|"
        elif len(str(card_number)) == 2:
            card = f"______\n|    |\n| {card_number} |\n|____|"
        print(colored(card, card_color))