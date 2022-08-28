from ..util.grids import Grid, GridRoutes

def get_answer() -> int:
    grid_routes = GridRoutes(21, 21)
    return grid_routes.get_number_of_routes((0, 0), (20, 20), (Grid.move_right, Grid.move_down))