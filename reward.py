class Reward:
    def __init__(self, description, reward_type):
        self.description = description
        self.type = reward_type

    def show(self):
        print(self.description)