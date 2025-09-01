DIRECTIONS = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]
DIRECTIONS.remove((0, 0))

class Plate:
    """
    The main class of the game, Holds and proccess the cells and it's states.
        Cell states:
            - True -> Alive.
            - False -> Dead.
    """
    def __init__(self, size: tuple[int, int], rules: tuple[int, int, int] = (2, 3, 4), history_size: int = 8):
        """
        Creates the plate.
        - size: tuple[int, int] -> The size of the grid (width, height).
        - rules: tuple[int, int, int] -> The rules of the game.
        - history_size: int -> How many states can be saved in history (not implemented).
        """
        self.width, self.height = size
        self.grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.rules = rules
        self.updated = True

    def set_cell(self, position: tuple[int, int], state: bool):
        """
        Sets the state of the cell in the `position`.
        - position: tuple[int, int] -> The position of the cell (y, x).
        - state: bool -> The new state of the cell (True = Alive, False = Dead).
        """
        if not self.is_valid_cell(position): raise IndexError("Cell not found.")
        y, x = position
        self.grid[y][x] = state

    def get_cell(self, position: tuple[int, int]) -> bool:
        """
        Gets the state of the cell in the `postion`.
        - position: tuple[int, int] -> The position of the cell (y, x).
        """
        #if not self.is_valid_cell(position): raise IndexError("Cell not found.")
        y, x = position
        return self.is_valid_cell(position) and self.grid[y][x]

    def is_valid_cell(self, position: tuple[int, int]) -> bool:
        """
        Returns `True` if is a valid cell position in the grid, else returns `False`.
        - position: tuple[int, int] -> The position of the cell (y, x).
        """
        y, x = position
        return (x < self.width) and (x >= 0) and (y < self.height) and (y >= 0)
    
    def next_state(self) -> list[list[int]]:
        new_state = [[False for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_state[y][x] = self.process((y, x))

        self.updated = self.grid != new_state
        self.grid = new_state
        return new_state

    def process(self, position) -> bool:
        y, x = position
        count = 0
        for neighbour in [(y+ direction[0], x + direction[1]) for direction in DIRECTIONS]:
            if self.get_cell(neighbour):
                count += 1

        isolated = count < self.rules[0]
        born = count >= self.rules[1]
        sufocated = count >= self.rules[2]

        if isolated or sufocated: return False
        if born: return True
        return self.get_cell(position)
    
    # Overrides
    def __str__(self):
        canvas = ""
        for y in range(self.height):
            for x in range(self.width):
                canvas += "# " if self.get_cell((y, x)) else "· "
            canvas += "\n"

        return canvas
