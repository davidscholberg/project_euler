from ..util.grids import Grid, UpDiagonalGridIndicesIterator, DownDiagonalGridIndicesIterator

def get_answer() -> int:
    grid_size = 1001
    spiral_grid = Grid(grid_size, grid_size)
    spiral_grid.make_integer_spiral()
    up_diagonal_sum = sum(map(lambda c: spiral_grid.get(c), next(UpDiagonalGridIndicesIterator(grid_size, grid_size, grid_size))))
    down_diagonal_sum = sum(map(lambda c: spiral_grid.get(c), next(DownDiagonalGridIndicesIterator(grid_size, grid_size, grid_size))))
    return up_diagonal_sum + down_diagonal_sum - 1