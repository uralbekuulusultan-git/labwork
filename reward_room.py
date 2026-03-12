from room import Room

class RewardRoom(Room):
    def __init__(self, number, description, reward):
        super().__init__(number, description)
        self.reward = reward
        self.cleaned = False

    def show_description(self):
        super().show_description()
        if self.cleaned:
            print("✔ Награда уже получена")

    def get_reward(self, player):
        if self.cleaned:
            print("Награда уже получена")
            return
        player.rewards.append(self.reward)
        self.cleaned = True
        self.visited = True
        print("\nВы получили награду:")
        self.reward.show()