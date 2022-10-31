from typing import Callable, Iterator

class Grid:
    def __init__(self, grid_data = None, rows = None, columns = None, from_grid = None, default_value = 0) -> None:
        self._grid = []
        if grid_data is not None:
            self._create_grid_from_data(grid_data)
        elif rows is not None:
            self._create_grid_from_dimensions(rows, columns, default_value)
        elif from_grid is not None:
            self._create_grid_from_grid(from_grid, default_value)

    def _create_grid_from_data(self, grid_data: str) -> None:
        for row in grid_data.split('\n'):
            if row == '':
                continue
            self._grid.append(list(map(int, row.split(' '))))

    def _create_grid_from_dimensions(self, rows: int, columns, default_value) -> None:
        if columns is None:
            columns = rows
        for _ in range(0, rows):
            self._grid.append([default_value] * columns)

    def _create_grid_from_grid(self, grid, default_value) -> None:
        for row in grid._grid:
            self._grid.append([default_value] * len(row))

    def bottom_left(self) -> tuple[int, int]:
        return (len(self._grid) - 1, 0)

    def bottom_right(self) -> tuple[int, int]:
        last_row = len(self._grid) - 1
        return (last_row, len(self._grid[last_row]) - 1)

    def get(self, coordinate: tuple[int, int]):
        return self._grid[coordinate[0]][coordinate[1]]

    def in_bounds(self, coordinate: tuple[int, int]) -> bool:
        return (
            coordinate[0] >= 0 and coordinate[0] < len(self._grid) and
            coordinate[1] >= 0 and coordinate[1] < len(self._grid[coordinate[0]])
        )

    def is_on_bottom_edge(self, coordinate: tuple[int, int]) -> bool:
        return self.in_bounds(coordinate) and coordinate[0] == len(self._grid) - 1

    def is_on_left_edge(self, coordinate: tuple[int, int]) -> bool:
        return self.in_bounds(coordinate) and coordinate[1] == 0

    def is_on_right_edge(self, coordinate: tuple[int, int]) -> bool:
        return self.in_bounds(coordinate) and coordinate[1] == len(self._grid[coordinate[0]]) - 1

    def is_on_top_edge(self, coordinate: tuple[int, int]) -> bool:
        return self.in_bounds(coordinate) and coordinate[0] == 0

    def set(self, coordinate: tuple[int, int], value):
        self._grid[coordinate[0]][coordinate[1]] = value

    def top_left(self) -> tuple[int, int]:
        return (0, 0)

    def top_right(self) -> tuple[int, int]:
        return (0, len(self._grid[0]) - 1)