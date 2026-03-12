from generator import GameGenerator
from player import Player

def main():
    generator = GameGenerator()
    rooms = generator.generate_rooms()
    rewards_pool = generator.create_rewards()
    player = Player(rooms[0], rewards_pool)

    while True:
        result = player.interact_with_room()
        if result == "restart":
            print("Вы сдались. Игра начинается заново.")
            return main()

        player.move_to_room()

        visited = sum(1 for r in rooms if r.visited)
        print(f"\nПрогресс: {visited}/10")
        if visited >= 10:
            print("\nВы победили!")
            break

if __name__ == "__main__":
    main()