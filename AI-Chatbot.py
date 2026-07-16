import datetime
import random

class DecodeBot:

    def __init__(self):
        self.bot_name = "DecodeBot"
        self.user_name = ""
        self.jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the Python developer wear glasses? Because they couldn't C#!",
            "Debugging is like being a detective in a crime movie where you are also the criminal."
        ]

        self.quotes = [
            "Success comes to those who never stop learning.",
            "Practice makes a programmer perfect.",
            "Every expert was once a beginner.",
            "Stay positive and keep coding!"
        ]

        self.facts = [
            "Python was created by Guido van Rossum in 1991.",
            "The first computer programmer was Ada Lovelace.",
            "Python is one of the world's most popular programming languages."
        ]

    def greet(self):
        print("=" * 50)
        print("      Welcome to DecodeLabs AI Chatbot")
        print("=" * 50)

        self.user_name = input("Enter your name: ").strip()

        if self.user_name == "":
            self.user_name = "Guest"

        print(f"\nHello {self.user_name}! 😊")
        print("Type 'help' to see available commands.\n")

    def show_help(self):
        print("\n========== COMMANDS ==========")
        print("hello       -> Greeting")
        print("time        -> Current Time")
        print("date        -> Current Date")
        print("joke        -> Random Joke")
        print("quote       -> Motivational Quote")
        print("fact        -> Fun Fact")
        print("calc        -> Calculator")
        print("about       -> About Bot")
        print("help        -> Show Commands")
        print("bye         -> Exit")
        print("==============================\n")

    def current_time(self):
        now = datetime.datetime.now()
        print("Current Time:", now.strftime("%I:%M:%S %p"))

    def current_date(self):
        today = datetime.datetime.now()
        print("Today's Date:", today.strftime("%d-%m-%Y"))

    def tell_joke(self):
        print(random.choice(self.jokes))

    def tell_quote(self):
        print(random.choice(self.quotes))

    def tell_fact(self):
        print(random.choice(self.facts))

    def calculator(self):
        try:
            print("\nCalculator")
            num1 = float(input("First Number: "))
            operator = input("Operator (+ - * /): ")
            num2 = float(input("Second Number: "))

            if operator == "+":
                print("Result =", num1 + num2)
            elif operator == "-":
                print("Result =", num1 - num2)
            elif operator == "*":
                print("Result =", num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result =", num1 / num2)
            else:
                print("Invalid Operator.")

        except:
            print("Invalid Input.")

    def about(self):
        print("\nDecodeBot Version 1.0")
        print("A Rule-Based AI Chatbot")
        print("Developed in Python using Object-Oriented Programming.\n")

    def unknown(self):
        responses = [
            "Sorry, I didn't understand.",
            "Please type 'help' to see commands.",
            "Try another command."
        ]
        print(random.choice(responses))

    def run(self):
        self.greet()

        while True:
            command = input(f"{self.user_name}: ").lower().strip()

            if command == "hello":
                print(f"Hello {self.user_name}! 👋")

            elif command == "time":
                self.current_time()

            elif command == "date":
                self.current_date()

            elif command == "joke":
                self.tell_joke()

            elif command == "quote":
                self.tell_quote()

            elif command == "fact":
                self.tell_fact()

            elif command == "calc":
                self.calculator()

            elif command == "about":
                self.about()

            elif command == "help":
                self.show_help()

            elif command == "bye":  # <-- Yahan indentation theek ki
                print(f"\nGoodbye {self.user_name}! Have a great day. 👋")
                break

            else:
                self.unknown()

if __name__ == "__main__":
    bot = DecodeBot()
    bot.run()