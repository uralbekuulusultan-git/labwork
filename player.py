import random

class Player:
    def __init__(self, start_room, rewards_pool):
        self.current_room = start_room
        self.rewards = random.choices(rewards_pool, k=3)

    def show_rewards(self):
        print("\nВаши награды:")
        if not self.rewards:
            print("Нет наград")
            return
        for i, reward in enumerate(self.rewards, 1):
            print(f"{i}. {reward.description} ({reward.type})")

    def use_reward(self, room):
        if not self.rewards:
            print("У вас нет наград")
            return
        self.show_rewards()
        try:
            choice = int(input("Выберите номер награды: ")) - 1
        except ValueError:
            print("Введите число")
            return

        if choice < 0 or choice >= len(self.rewards):
            print("Неверный номер")
            return

        reward = self.rewards.pop(choice)
        if reward.type == "reset":
            room.wrong_attempts = 0
            room.blocked = False
            print("Попытки сброшены. Попробуйте снова решить загадку.")
        elif reward.type == "skip":
            print("Вы пропустили загадку")
            room.solved = True
            return True

    def move_to_room(self):
        room = self.current_room
        print("\nКуда идти?")
        for direction in room.neighboring_rooms:
            print(f"- {direction}")
        direction = input("Введите направление: ")
        if direction not in room.neighboring_rooms:
            print("Нельзя идти туда")
            return
        self.current_room = room.neighboring_rooms[direction]

    def interact_with_room(self):
        from challenge_room import ChallengeRoom
        from reward_room import RewardRoom

        room = self.current_room
        room.show_description()

        if isinstance(room, ChallengeRoom):

            while not room.solved:

                # Заблокированная комната
                if room.blocked:
                    print("\nКомната заблокирована! Что хотите сделать?")
                    print("1 - Использовать награду")
                    print("2 - Вернуться назад")
                    action = input("Ваш выбор: ")
                    if action == "1":
                        reset_or_skip = self.use_reward(room)
                        if not room.blocked:
                            continue  # комната разблокирована, можно снова отвечать
                        if room.solved:  # skip
                            return
                    elif action == "2":
                        if "назад" in room.neighboring_rooms:
                            self.current_room = room.neighboring_rooms["назад"]
                        return
                    else:
                        print("Неверный выбор")
                        continue
                else:
                    # Комната не заблокирована
                    print("\nЧто хотите сделать?")
                    print("1 - Ответить на загадку")
                    print("2 - Использовать награду")
                    # Убираем вариант "3 - Вернуться назад"
                    action = input("Ваш выбор: ")

                    if action == "1":
                        result = room.solve_challenge()
                        if result == "restart":
                            return "restart"
                        if room.solved:
                            print("Загадка решена! Можно идти дальше.")
                            return
                    elif action == "2":
                        skip = self.use_reward(room)
                        if skip:
                            return
                    else:
                        print("Неверный выбор")
                        continue

        elif isinstance(room, RewardRoom):
            room.get_reward(self)