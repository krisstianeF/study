# Player interface

```python
from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        x, y = random.choice(self.moves)
        self.position = (self.position[0] + x, self.position[1] + y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def level_up(self):
        diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonals)

# --- Usage demonstration ---
if __name__ == "__main__":
    pawn = Pawn()
    print("Initial position:", pawn.position)
    print("Initial moves:", pawn.moves)

    # Move 5 times with orthogonal moves only
    print("\nMaking 5 moves (orthogonal):")
    for step in range(1, 6):
        new_pos = pawn.make_move()
        print(f"Step {step}: moved to {new_pos}")

    print("\nPath so far:", pawn.path)

    # Level up – now diagonal moves become available
    pawn.level_up()
    print("\nMoves after level-up:", pawn.moves)

    # Move 5 more times (now diagonal moves may appear)
    print("\nMaking 5 more moves (could be diagonal):")
    for step in range(6, 11):
        new_pos = pawn.make_move()
        print(f"Step {step}: moved to {new_pos}")

    print("\nFinal path:", pawn.path)
    print("Final position:", pawn.position)
```
