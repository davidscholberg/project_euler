def get_answer() -> int:
    set_of_powers = set()
    for i in range(2, 101):
        for j in range(2, 101):
            set_of_powers.add(i ** j)
    return len(set_of_powers)