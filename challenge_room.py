from room import Room

class ChallengeRoom(Room):
    def __init__(self, number, description, challenge):
        super().__init__(number, description)
        self.challenge = challenge
        self.solved = False
        self.blocked = False
        self.wrong_attempts = 0

    def show_description(self):
        super().show_description()
        if self.solved:
            print("✔ Загадка уже решена")

    def solve_challenge(self):
        self.challenge.show_question()
        answer = input("Ваш ответ: ")
        if answer.strip().lower() == "сдаюсь":
            return "restart"
        if self.challenge.check_answer(answer):
            print("Правильно!")
            self.solved = True
            self.visited = True
            return True
        else:
            self.wrong_attempts += 1
            print("Неверно")
            print(f"Осталось попыток: {3 - self.wrong_attempts}")
            if self.wrong_attempts >= 3:
                self.blocked = True
                print("Комната заблокирована")
            return False