def square_even(vals):
    return [i**2 for i in vals if i % 2 == 0]

square_list = square_even([4, 5, 2, 2, 6, 7, 1, 5, 6])
square_set = set(square_list)

print(square_set)



