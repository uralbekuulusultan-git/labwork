class Reward:
    RESET = "reset"
    SKIP = "skip"

    def __init__(self, description: str, reward_type: str):
        self.description = description
        self.type = reward_type

    def show(self):
        print(f"{self.description} ({self.type})")
