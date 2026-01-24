# ==============================
# QUIZ GAME WITH USER PROFILES
# ==============================

import csv
from datetime import datetime

# Quiz Questions
# Each question is stored as a dictionary
# All questions together are stored in a list

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. function", "C. def", "D. define"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["A. while", "B. for", "C. if", "D. loop"],
        "answer": "B"
    }
]

# Function: Run the Quiz
def run_quiz():
    score = 0  # keeps track of correct answers

    # Loop through each question
    for q in questions:
        print("\n" + q["question"])

        # Display options
        for option in q["options"]:
            print(option)

        # Take user answer
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # Validate input
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input! Enter A/B/C/D only: ").upper()

        # Check answer
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}")

    return score


# Function: Save Score to CSV
def save_score(username, score):
    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open CSV file in append mode
    with open("scores.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score, timestamp])


# Function: Display Leaderboard
def show_leaderboard():
    scores = []

    try:
        # Read scores from CSV file
        with open("scores.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(row)
    except FileNotFoundError:
        print("\nNo scores available yet.")
        return

    # Function used for sorting (NO lambda)
    def get_score(record):
        return int(record[1])
    
    # Sort scores by score (highest first)
    scores.sort(key=get_score, reverse=True)

    print("\nLEADERBOARD (Top 5)")
    print("-" * 30)

    # Display top 5 scores
    for i, record in enumerate(scores[:5], start=1):
        print(f"{i}. {record[0]} - {record[1]} points on {record[2]}")


# MAIN PROGRAM
def main():
    print("Welcome to the Python Quiz Game")

    # Ask user name
    username = input("Enter your name: ")

    # Run quiz
    final_score = run_quiz()

    # Display final score
    print("\nQuiz Completed!")
    print(f"{username}, your final score is {final_score}/{len(questions)}")

    # Save score
    save_score(username, final_score)

    # Show leaderboard
    show_leaderboard()


# Run the program
main()
