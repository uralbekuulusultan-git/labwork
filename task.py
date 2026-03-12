class Task:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def show_question(self):
        print("\nЗагадка:")
        print(self.question)

    def check_answer(self, user_answer: str) -> bool:
        return user_answer.strip().lower() == self.answer.strip().lower()
