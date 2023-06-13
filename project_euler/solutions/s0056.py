from project_euler.util.digits.digits import digits

def get_answer() -> int:
    max_power_sum = 0
    for base in range(2, 100):
        for exponent in range(1, 100):
            power = base ** exponent
            power_sum = sum(digits(power))
            if power_sum > max_power_sum:
                max_power_sum = power_sum
    return max_power_sum