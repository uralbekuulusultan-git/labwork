import random

from challenge_room import ChallengeRoom
from reward import Reward
from reward_room import RewardRoom


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
            return None

        self.show_rewards()
        try:
            choice = int(input("Выберите номер награды: ")) - 1
        except ValueError:
            print("Введите корректное число")
            return None

        if choice < 0 or choice >= len(self.rewards):
            print("Неверный номер")
            return None

        reward = self.rewards.pop(choice)

        if reward.type == Reward.RESET:
            room.wrong_attempts = 0
            room.blocked = False
            print("🔄 Попытки сброшены, комната разблокирована")
            return Reward.RESET

        if reward.type == Reward.SKIP:
            print("⏭ Вы проскочили комнату (она не засчитана как пройденная)")
            return Reward.SKIP

        print("Неизвестный тип награды")
        return None

    def move_to_room(self, allow_forward_from_unsolved=False):
        room = self.current_room
        available = dict(room.neighboring_rooms)

        if isinstance(room, ChallengeRoom) and not room.solved and not allow_forward_from_unsolved:
            available = {k: v for k, v in available.items() if k == "назад"}
            if not available:
                print("Вы не можете пройти дальше, пока не решите загадку.")
                return False
            print("Пока загадка не решена, можно идти только назад.")

        print("\nКуда идти?")
        for direction in available:
            print(f"- {direction}")

        direction = input("Введите направление: ").strip().lower()
        if direction not in available:
            print("Нельзя идти в этом направлении")
            return False

        self.current_room = available[direction]
        return True

    def interact_with_room(self):
        room = self.current_room
        room.show_description()

        if isinstance(room, RewardRoom):
            room.get_reward(self)
            return "ok"

        if isinstance(room, ChallengeRoom):
            if room.solved:
                return "ok"

            while True:
                if room.blocked:
                    print("\n1 - Использовать награду")
                    print("2 - Вернуться назад")
                    action = input("Ваш выбор: ").strip()

                    if action == "1":
                        effect = self.use_reward(room)
                        if effect == Reward.SKIP:
                            return "skipped"
                    elif action == "2":
                        if "назад" in room.neighboring_rooms:
                            self.current_room = room.neighboring_rooms["назад"]
                        else:
                            print("Назад идти некуда")
                        return "ok"
                    else:
                        print("Неверный выбор")
                    continue

                print("\n1 - Ответить на загадку")
                print("2 - Использовать награду")
                action = input("Ваш выбор: ").strip()

                if action == "1":
                    result = room.solve_challenge()
                    if result == "restart":
                        return "restart"
                    if result is True:
                        return "ok"
                elif action == "2":
                    effect = self.use_reward(room)
                    if effect == Reward.SKIP:
                        return "skipped"
                else:
                    print("Неверный выбор")
