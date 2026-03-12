class Room:
    def __init__(self, number: int, description: str):
        self.number = number
        self.description = description
        self.visited = False
        self.neighboring_rooms = {}

    def show_description(self):
        print("\n" + "=" * 50)
        print(f"Комната №{self.number}")
        print(self.description)
        if self.visited:
            print("✔ Комната уже засчитана")
        print("=" * 50)

    def show_directions(self):
        print("\nДоступные направления:")
        for direction in self.neighboring_rooms:
            print(f"- {direction}")
