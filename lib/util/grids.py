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

class Lattice:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows = rows
        self._columns = columns
        self._lattice = self._create_lattice()

    def move_right(self, coordinates: tuple) -> tuple:
        return (coordinates[0], coordinates[1] + 1)

    def move_down(self, coordinates: tuple) -> tuple:
        return (coordinates[0] + 1, coordinates[1])

    # Calling this function multiple times is only valid if to_coordinates and allowed_moves doesn't change.
    def get_number_of_routes(self, from_coordinates: tuple, to_coordinates: tuple, allowed_moves: tuple) -> int:
        if self._coordinates_are_out_of_bounds(from_coordinates) or self._coordinates_are_out_of_bounds(to_coordinates):
            return 0
        if self._lattice[from_coordinates[0]][from_coordinates[1]] != -1:
            return self._lattice[from_coordinates[0]][from_coordinates[1]]
        if self._coordinates_are_equal(from_coordinates, to_coordinates):
            self._lattice[from_coordinates[0]][from_coordinates[1]] = 1
            return 1
        route_count = 0
        for move in allowed_moves:
            route_count += self.get_number_of_routes(move(from_coordinates), to_coordinates, allowed_moves)
        self._lattice[from_coordinates[0]][from_coordinates[1]] = route_count
        return route_count

    def _create_lattice(self) -> list:
        lattice = []
        for i in range(self._rows + 1):
            lattice.append([-1] * (self._columns + 1))
        return lattice

    def _coordinates_are_equal(self, a: tuple, b: tuple) -> bool:
        return a[0] == b[0] and a[1] == b[1]

    def _coordinates_are_out_of_bounds(self, coordinates: tuple) -> bool:
        return coordinates[0] < 0 or coordinates[1] < 0 or coordinates[0] > self._rows or coordinates[1] > self._columns