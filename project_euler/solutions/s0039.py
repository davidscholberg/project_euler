from project_euler.util.sums.pythagorean_triplet import pythagorean_triplets

def get_answer() -> int:
    perimeter_with_max_triplets = 0
    max_triplets = 0
    for perimeter in range(3, 1001):
        triplet_count = len(pythagorean_triplets(perimeter))
        if triplet_count > max_triplets:
            max_triplets = triplet_count
            perimeter_with_max_triplets = perimeter
    return perimeter_with_max_triplets