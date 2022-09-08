class GridIndicesIterator:
    def __init__(self, n: int, row_count: int, column_count: int) -> None:
        self._n = n
        self._row_count = row_count
        self._column_count = column_count
        self._row = 0
        self._column = 0

    def __iter__(self):
        return self

class HorizontalGridIndicesIterator(GridIndicesIterator):
    def __next__(self) -> tuple:
        if self._column > self._column_count - self._n:
            if self._row >= self._row_count - 1:
                raise StopIteration
            self._row += 1
            self._column = 0
        indices = []
        for i in range(self._n):
            indices.append((self._row, self._column + i))
        self._column += 1
        return tuple(indices)

class VerticalGridIndicesIterator(GridIndicesIterator):
    def __next__(self) -> tuple:
        if self._row > self._row_count - self._n:
            if self._column >= self._column_count - 1:
                raise StopIteration
            self._column += 1
            self._row = 0
        indices = []
        for i in range(self._n):
            indices.append((self._row + i, self._column))
        self._row += 1
        return tuple(indices)

class UpDiagonalGridIndicesIterator(GridIndicesIterator):
    def __init__(self, n: int, row_count: int, column_count: int) -> None:
        super().__init__(n, row_count, column_count)
        self._row = self._n - 1
        self._column = 0
        self._row_max = self._row

    def __next__(self) -> tuple:
        if self._row > self._row_count - 1:
            raise StopIteration
        if self._column > self._column_count - self._n:
            raise StopIteration
        indices = []
        for i in range(self._n):
            indices.append((self._row - i, self._column + i))
        if self._row == self._n - 1 or self._column == self._column_count - self._n:
            old_row = self._row
            self._row = self._row_max + 1
            if self._row > self._row_count - 1:
                self._row = self._row_count - 1
            if self._row > self._row_max:
                self._row_max = self._row
            self._column -= self._row - old_row - 1
        else:
            self._row -= 1
            self._column += 1
        return tuple(indices)

class DownDiagonalGridIndicesIterator(GridIndicesIterator):
    def __init__(self, n: int, row_count: int, column_count: int) -> None:
        super().__init__(n, row_count, column_count)
        self._row = self._row_count - self._n
        self._column = 0
        self._row_min = self._row

    def __next__(self) -> tuple:
        if self._row < 0:
            raise StopIteration
        if self._column > self._column_count - self._n:
            raise StopIteration
        indices = []
        for i in range(self._n):
            indices.append((self._row + i, self._column + i))
        if self._row == self._row_count - self._n or self._column == self._column_count - self._n:
            old_row = self._row
            self._row = self._row_min - 1
            if self._row < 0:
                self._row = 0
            if self._row < self._row_min:
                self._row_min = self._row
            self._column -= old_row - self._row - 1
        else:
            self._row += 1
            self._column += 1
        return tuple(indices)

class Grid:
    def __init__(self, rows: int, columns: int, create_grid: bool = True) -> None:
        self._rows = rows
        self._columns = columns
        self._grid = []
        if create_grid:
            self._grid = self._create_grid()

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    @staticmethod
    def move_right(coordinates: tuple) -> tuple:
        return (coordinates[0], coordinates[1] + 1)

    @staticmethod
    def move_left(coordinates: tuple) -> tuple:
        return (coordinates[0], coordinates[1] - 1)

    @staticmethod
    def move_up(coordinates: tuple) -> tuple:
        return (coordinates[0] - 1, coordinates[1])

    @staticmethod
    def move_down(coordinates: tuple) -> tuple:
        return (coordinates[0] + 1, coordinates[1])

    @staticmethod
    def move_down_right(coordinates: tuple) -> tuple:
        return (coordinates[0] + 1, coordinates[1] + 1)

    def get(self, coordinates: tuple) -> int:
        return self._grid[coordinates[0]][coordinates[1]]

    def set(self, coordinates: tuple, n: int) -> None:
        self._grid[coordinates[0]][coordinates[1]] = n

    @staticmethod
    def coordinates_are_equal(a: tuple, b: tuple) -> bool:
        return a[0] == b[0] and a[1] == b[1]

    def coordinates_are_out_of_bounds(self, coordinates: tuple) -> bool:
        return coordinates[0] < 0 or coordinates[1] < 0 or coordinates[0] >= self._rows or coordinates[1] >= self._columns

    def make_integer_spiral(self) -> None:
        spiral_counter = 1
        coordinates = (self._rows // 2, self._columns // 2)
        if self.coordinates_are_out_of_bounds(coordinates):
            return
        self.set(coordinates, spiral_counter)
        spiral_counter += 1
        moves = (self.move_right, self.move_down, self.move_left, self.move_up)
        move_counter = 0
        while True:
            for move in moves:
                if move == self.move_right or move == self.move_left:
                    move_counter += 1
                for _ in range(move_counter):
                    coordinates = move(coordinates)
                    if self.coordinates_are_out_of_bounds(coordinates):
                        return
                    self.set(coordinates, spiral_counter)
                    spiral_counter += 1

    def _create_grid(self) -> list:
        grid = []
        for i in range(self._rows):
            grid.append([-1] * (self._columns))
        return grid

class GridRoutes:
    def __init__(self, rows: int, columns: int) -> None:
        self._route_count_cache = Grid(rows, columns)

    # Calling this function multiple times is only valid if to_coordinates and allowed_moves doesn't change.
    def get_number_of_routes(self, from_coordinates: tuple, to_coordinates: tuple, allowed_moves: tuple) -> int:
        if self._route_count_cache.coordinates_are_out_of_bounds(from_coordinates) or self._route_count_cache.coordinates_are_out_of_bounds(to_coordinates):
            return 0
        cached_route_count = self._route_count_cache.get(from_coordinates)
        if cached_route_count != -1:
            return cached_route_count
        if self._route_count_cache.coordinates_are_equal(from_coordinates, to_coordinates):
            self._route_count_cache.set(from_coordinates, 1)
            return 1
        route_count = 0
        for move in allowed_moves:
            route_count += self.get_number_of_routes(move(from_coordinates), to_coordinates, allowed_moves)
        self._route_count_cache.set(from_coordinates, route_count)
        return route_count

class TriangleGrid(Grid):
    def __init__(self, rows: int = -1, create_grid: bool = True, from_file: str = "") -> None:
        super().__init__(rows, -1, create_grid = False)
        if create_grid:
            if from_file != "":
                self._create_grid_from_file(from_file)
            elif rows != -1:
                self._create_empty_grid()

    def _create_grid_from_file(self, filename: str) -> None:
        with open(filename) as f:
            for line in f:
                self._grid.append(list(map(int, line.split())))
        self._rows = len(self._grid)

    def _create_empty_grid(self) -> None:
        for i in range(self._rows):
            self._grid.append([-1] * (i + 1))

    def coordinates_are_out_of_bounds(self, coordinates: tuple) -> bool:
        return \
            coordinates[0] < 0 or \
            coordinates[0] > self._rows - 1 or \
            coordinates[1] < 0 or \
            coordinates[1] > coordinates[0]

class TriangleGridSum:
    def __init__(self, triangle_grid_filename: str) -> None:
        self._triangle_grid = TriangleGrid(from_file = triangle_grid_filename)
        self._max_sum_cache = TriangleGrid(rows = self._triangle_grid.rows)

    # Calling this function multiple times is only valid if allowed_moves doesn't change.
    def get_max_sum_from_coordinates_to_bounds(self, from_coordinates: tuple, allowed_moves: tuple) -> int:
        if self._triangle_grid.coordinates_are_out_of_bounds(from_coordinates):
            return 0
        cached_max_sum = self._max_sum_cache.get(from_coordinates)
        if cached_max_sum != -1:
            return cached_max_sum
        max_child_sum = 0
        for move in allowed_moves:
            child_sum = self.get_max_sum_from_coordinates_to_bounds(move(from_coordinates), allowed_moves)
            if child_sum > max_child_sum:
                max_child_sum = child_sum
        max_sum = max_child_sum + self._triangle_grid.get(from_coordinates)
        self._max_sum_cache.set(from_coordinates, max_sum)
        return max_sum