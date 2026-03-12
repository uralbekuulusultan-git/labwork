import random
import json

from challenge_room import ChallengeRoom
from reward_room import RewardRoom
from task import Task
from reward import Reward

class GameGenerator:
    def load_tasks(self):
        with open("riddles.json", encoding="utf-8") as f:
            data = json.load(f)
        tasks = [Task(r["question"], r["answer"]) for r in data]
        random.shuffle(tasks)
        return tasks

    def create_rewards(self):
        return [
            Reward("Сбросить попытки", "reset"),
            Reward("Пропустить загадку", "skip")
        ]

    def generate_rooms(self):
        tasks = self.load_tasks()
        rewards = self.create_rewards()
        rooms = []

        for i in range(100):
            if random.random() < 0.7 and tasks:
                task = tasks.pop()
                room = ChallengeRoom(i, "Комната с загадкой", task)
            else:
                reward = random.choice(rewards)
                room = RewardRoom(i, "Комната с наградой", reward)
            rooms.append(room)

        directions = ["прямо", "налево", "направо"]

        for i in range(len(rooms)-1):
            count = random.randint(1, 3)
            dirs = random.sample(directions, count)
            for d in dirs:
                rooms[i].neighboring_rooms[d] = rooms[i+1]
            rooms[i+1].neighboring_rooms["назад"] = rooms[i]

        return rooms