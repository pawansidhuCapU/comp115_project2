class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


def run_quiz(questions):
    score = 0
    for question in questions:
        question.display_question()
        user_answer = input("Enter your answer (1, 2, 3, 4): ")
        if question.check_answer(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    print(f"Quiz completed! You scored {score} out of {len(questions)}.")


# Sample questions
question1 = Question("What is the capital of France?",
                     ["Paris", "London", "Berlin", "Rome"], "1")
question2 = Question("Which planet is known as the Red Planet?",
                     ["Mars", "Venus", "Jupiter", "Mercury"], "1")
question3 = Question("Who wrote the play 'Romeo and Juliet'?",
                     ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "1")

# List of questions
questions = [question1, question2, question3]

# Run the quiz
run_quiz(questions)



 




    






