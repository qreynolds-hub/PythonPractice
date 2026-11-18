
import random


def main():
    # Dictionary containing states and their capitals
    states = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Michigan": "Lansing",
        "New York": "Albany",
        "New Hampshire": "Concord",
        "Ohio": "Columbus",
        "Texas": "Austin",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
        "Oregon": "Salem"
    }

    correct = 0
    incorrect = 0

    # Continue asking questions until the user quits
    while True:
        state = random.choice(list(states.keys()))

        answer = input(
            f"What is the capital of {state}? (or enter 0 to quit): "
        ).strip()

        # Check if the user wants to quit
        if answer == "0":
            break

        # Check whether the answer is correct
        if answer.lower() == states[state].lower():
            print("That is correct.")
            correct += 1
        else:
            print("That is incorrect.")
            incorrect += 1

    # Display the final game summary
    print(
        f"You had {correct} correct responses and "
        f"{incorrect} incorrect responses."
    )


if __name__ == "__main__":
    main()
