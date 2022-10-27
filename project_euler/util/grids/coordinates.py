def move_up(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return (coordinate[0] - step, coordinate[1])

def move_down(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return (coordinate[0] + step, coordinate[1])

def move_left(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return (coordinate[0], coordinate[1] - step)

def move_right(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return (coordinate[0], coordinate[1] + step)

def move_up_left(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return move_up(move_left(coordinate, step), step)

def move_up_right(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return move_up(move_right(coordinate, step), step)

def move_down_left(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return move_down(move_left(coordinate, step), step)

def move_down_right(coordinate: tuple[int, int], step: int = 1) -> tuple[int, int]:
    return move_down(move_right(coordinate, step), step)