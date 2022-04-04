def my_func(p_1, p_2, p_3):
    t = [p_1, p_2, p_3]
    max_1 = max(t)
    t.remove(max_1)
    max_2 = max(t)
    return max_1 + max_2


print(my_func(3, 2, 7))