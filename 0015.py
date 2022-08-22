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

lattice = Lattice(20, 20)
answer = lattice.get_number_of_routes((0, 0), (20, 20), (lattice.move_right, lattice.move_down))
print(answer)