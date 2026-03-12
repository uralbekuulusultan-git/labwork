class Room:
    def __init__(self, number, description):
        self.number = number
        self.description = description
        self.visited = False
        self.neighboring_rooms = {}

    def show_description(self):
        print("\n" + "=" * 50)
        print(f"Комната № {self.number}")
        print(self.description)
        if self.visited:
            print("⚠ Вы уже посещали эту комнату")
        print("=" * 50)

    def show_directions(self):
        print("\nДоступные направления:")
        for direction in self.neighboring_rooms:
            print(f"- {direction}")