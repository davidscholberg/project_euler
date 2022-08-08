def get_list_of_multiples_capped(multiple_of, multiple_cap):
    current_multiple = multiple_of
    list_of_multiples = []
    while current_multiple < multiple_cap:
        list_of_multiples.append(current_multiple)
        current_multiple += multiple_of
    return list_of_multiples

multiples_of_3 = get_list_of_multiples_capped(3, 1000)
multiples_of_5 = get_list_of_multiples_capped(5, 1000)
answer = sum(set(multiples_of_3 + multiples_of_5))
print(answer)
