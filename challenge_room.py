from room import Room


class ChallengeRoom(Room):
    MAX_WRONG_ATTEMPTS = 3

    def __init__(self, number, description, challenge):
        super().__init__(number, description)
        self.challenge = challenge
        self.solved = False
        self.blocked = False
        self.wrong_attempts = 0

    def show_description(self):
        super().show_description()
        if self.solved:
            print("✔ Загадка решена")
        elif self.blocked:
            print("⛔ Комната заблокирована (используйте сброс попыток)")
        else:
            print(f"Попыток до блокировки: {self.MAX_WRONG_ATTEMPTS - self.wrong_attempts}")

    def solve_challenge(self):
        if self.solved:
            print("Загадка уже решена.")
            return True

        self.challenge.show_question()
        answer = input("Ваш ответ (или 'сдаюсь'): ")
        if answer.strip().lower() == "сдаюсь":
            return "restart"

        if self.challenge.check_answer(answer):
            print("✅ Правильно!")
            self.solved = True
            self.visited = True
            return True

        self.wrong_attempts += 1
        print("❌ Неверно")
        left = self.MAX_WRONG_ATTEMPTS - self.wrong_attempts
        if left > 0:
            print(f"Осталось попыток: {left}")
        else:
            self.blocked = True
            print("⛔ Комната заблокирована после 3 ошибок")
        return False
