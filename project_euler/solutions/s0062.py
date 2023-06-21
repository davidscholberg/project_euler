from itertools import count

from project_euler.util.digits.digits import digit_count_map

def get_answer() -> int:
    cubes = map(lambda n: n ** 3, count(4))
    first_n_plus_one_digit_cube = 27
    for digit_count in count(2):
        n_digit_cubes = [first_n_plus_one_digit_cube]
        for cube in cubes:
            if cube >= 10 ** digit_count:
                first_n_plus_one_digit_cube = cube
                break
            n_digit_cubes.append(cube)
        seen_permutations = set()
        for i in range(0, len(n_digit_cubes) - 1):
            if n_digit_cubes[i] in seen_permutations:
                continue
            cube_permutations = [n_digit_cubes[i]]
            i_digit_count_map = digit_count_map(n_digit_cubes[i])
            for j in range(i + 1, len(n_digit_cubes)):
                if n_digit_cubes[j] in seen_permutations:
                    continue
                if i_digit_count_map == digit_count_map(n_digit_cubes[j]):
                    cube_permutations.append(n_digit_cubes[j])
                    if len(cube_permutations) == 5:
                        return n_digit_cubes[i]
            if len(cube_permutations) > 1:
                seen_permutations.update(cube_permutations)
    return 0