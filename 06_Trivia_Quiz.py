quiz = (
    ("What is the real name of 🐶?", "Dogesh"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What sound does a cow make?", "Moo"),
)

score = 0
for question, answer in quiz:
    user_ans = input(question + " ")
    if user_ans.strip().lower() == answer.lower():
        print("Correct! 7 Crore 😜")
        score += 1
    else:
        print("Wrong! 😬 The answer was:", answer)

print("You got", score, "out of", len(quiz))
