"""*/Battleship: Create a 8x8 map in python. Randomly place the following ships on this map:
a.⁠ ⁠An aircraft carrier that occupies 6x1 space
b.⁠ ⁠⁠A destroyer that occupies 4x1 space
c.⁠ ⁠⁠ A frigate that occupies 2x1 space
Two ships cannot occupy the same location and the ships cannot be placed diagonally. The ships cannot move.
The user is tasked on destroying the enemy fleet. They have to input coordinates for the next missile strike. 
The program will tell if they have hit or miss and count the number of tries it took the user to destroy the enemy fleet.*/"""
import random
class Battleship:
    def __init__(self):
        self.ship_coords = []
        self.guessed_coords = []
        self.total_hits = 0
        self.tries = 0
    def print_board(self):
        for i in range(8):
            for j in range(8):
                current_square = (i, j)
                if current_square in self.guessed_coords:
                    if current_square in self.ship_coords:
                        print(" X ", end="")
                    else:
                        print(" O ", end="")
                else:
                    print(" ~ ", end="")
            print()
    def place_ship(self, ship_size):
        placed = False
        while not placed:
            new_coords = []
            orientation = random.choice(['h', 'v'])
            if orientation == 'h':
                row = random.randint(0, 7)
                col = random.randint(0, 7 - ship_size)
                for i in range(ship_size):
                    new_coords.append((row, col + i))
            else:
                col = random.randint(0, 7)
                row = random.randint(0, 7 - ship_size)
                for i in range(ship_size):
                    new_coords.append((row + i, col))
            collision = False
            for coord in new_coords:
                if coord in self.ship_coords:
                    collision = True
                    break
            if not collision:
                self.ship_coords.extend(new_coords)
                placed = True 
    def battle(self):
        print("Enter coordinates to missile strike with a space between them")
        row, col = map(int, input().split())
        self.tries += 1
        hit_coords = (row, col)
        if hit_coords in self.guessed_coords:
            print("We have already hit that commander")
        else:
            self.guessed_coords.append(hit_coords)
            if hit_coords in self.ship_coords:
                print("You have hit a ship")
                self.total_hits += 1
            else:
                print("You have missed")
        self.print_board()

if __name__ == "__main__":
    game = Battleship()
    game.place_ship(2)
    game.place_ship(4)
    game.place_ship(6)
    print("Ready for battle")
    game.print_board()
    while game.total_hits < 12:
        game.battle()
    print(f"You took {game.tries} tries to sink the enemy fleet")