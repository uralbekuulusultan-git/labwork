from generator import GameGenerator
from player import Player


class Game:
    def __init__(self, win_target=10, total_rooms=100):
        self.generator = GameGenerator()
        self.rooms = self.generator.generate_rooms(total_rooms=total_rooms)
        rewards_pool = self.generator.create_rewards()
        self.player = Player(self.rooms[0], rewards_pool)
        self.win_target = win_target

    def progress(self):
        return sum(1 for room in self.rooms if room.visited)

    def run(self):
        while True:
            result = self.player.interact_with_room()

            if result == "restart":
                print("\nВы сдались. Игра перезапускается...\n")
                return "restart"

            print(f"\nПрогресс: {self.progress()}/{self.win_target}")
            if self.progress() >= self.win_target:
                print("\n🎉 Вы победили!")
                return "win"

            allow_forward = result == "skipped"
            self.player.move_to_room(allow_forward_from_unsolved=allow_forward)


def main():
    while True:
        game = Game()
        status = game.run()
        if status != "restart":
            break


if __name__ == "__main__":
    main()
