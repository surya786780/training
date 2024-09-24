quiz = {
    "What is 2 + 2?": "4",
    "Which keyword is used to define a function in Python?": "def",
    "What data type is the result of: 5 // 2?": "int",
    "Which Python function is used to get the length of a list?": "len()",
    "What is the output of: print(2 ** 3)?": "8",
    "Which of these is an immutable data type in Python: list, tuple, or dictionary?": "tuple",
    "How do you start a comment in Python?": "#",
    "What is the correct file extension for Python files?": ".py",
    "Which keyword is used for exception handling in Python?": "try",
    "What is the purpose of the 'self' keyword in a class method?": "Refers to the instance of the class",
    "What does the 'break' statement do in a loop?": "Exits the loop",
    "What is the smallest prime number?": "2"
}

score = 0

for question, correct_answer in quiz.items():
    print(question)  # Display the question
    user_answer = input("Your answer: ")  # Get the user's answer
    
    if user_answer.strip().lower() == correct_answer.lower():  
        print("Correct!\n")
        score += 1  
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")

print(f"Quiz finished! Your final score is: {score}/{len(quiz)}")
