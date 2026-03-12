import json
import random
from collections import deque

from challenge_room import ChallengeRoom
from reward import Reward
from reward_room import RewardRoom
from task import Task


class GameGenerator:
    DIRECTIONS = ["прямо", "налево", "направо"]

    def load_tasks(self):
        with open("riddles.json", encoding="utf-8") as file:
            data = json.load(file)

        tasks = [Task(item["question"], item["answer"]) for item in data]
        random.shuffle(tasks)
        return tasks

    def create_rewards(self):
        return [
            Reward("Обнулиться: сбросить ошибки и снять блокировку", Reward.RESET),
            Reward("Проскочить: пройти без ответа", Reward.SKIP),
        ]

    def _create_room(self, room_number, tasks, rewards):
        is_challenge = random.random() < 0.7

        if is_challenge:
            if tasks:
                task = tasks.pop()
            else:
                fallback_index = room_number + 1
                task = Task(
                    f"Резервная загадка №{fallback_index}: сколько будет {fallback_index}+0?",
                    str(fallback_index),
                )
            return ChallengeRoom(room_number, "Комната с загадкой", task)

        reward = random.choice(rewards)
        return RewardRoom(room_number, "Комната с наградой", reward)

    def generate_rooms(self, total_rooms=100):
        tasks = self.load_tasks()
        rewards = self.create_rewards()

        rooms = [self._create_room(i, tasks, rewards) for i in range(total_rooms)]

        queue = deque([0])
        next_room_index = 1

        while queue and next_room_index < total_rooms:
            parent_idx = queue.popleft()
            parent = rooms[parent_idx]

            branch_count = random.randint(1, 3)
            free_directions = [d for d in self.DIRECTIONS if d not in parent.neighboring_rooms]
            chosen_directions = random.sample(free_directions, min(branch_count, len(free_directions)))

            for direction in chosen_directions:
                if next_room_index >= total_rooms:
                    break

                child = rooms[next_room_index]
                parent.neighboring_rooms[direction] = child
                child.neighboring_rooms["назад"] = parent
                queue.append(next_room_index)
                next_room_index += 1

        return rooms
