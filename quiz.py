# 1. Initialization (score, questions)
questions = [
    {"question": "Capitale of the United Kingdom ?", "answer": "london"},
    {"question": "2 + 2 ?", "answer": "4"},
    {"question": "Number of the letters in the alphabet ?", "answer": "26"}, 
    {"question": "French population ? (millions)", "answer": "69"}, 
    {"question": "Name of the  French president?", "answer": "macron"}
]

score = 0

# 2. Loop for the questions
for q in questions:
    answer_user = input(q["question"] + " ").strip().lower()

    if answer_user == q["answer"]:
        print("Good answer !")
        score += 1
    else:
        print(f"Wrong answer. The correct answer was {q['answer'].capitalize()}.")

# 3. Display of the final score
total_questions = len(questions)
print(f"Final Score : {score}/{total_questions}")

# 5. Message according to the score
if score <= 2:
    print("Let's revise basics.")
elif score <= 4:
    print("Not bad, an effort again.")
else:
    print("Perfect !")