from ..util.grids import Lattice

def get_answer() -> int:
    lattice = Lattice(20, 20)
    return lattice.get_number_of_routes((0, 0), (20, 20), (lattice.move_right, lattice.move_down))