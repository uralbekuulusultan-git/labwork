class Task:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def show_question(self):
        print("\nЗагадка:")
        print(self.question)
        print(f"(Ответ: {self.answer})")

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()