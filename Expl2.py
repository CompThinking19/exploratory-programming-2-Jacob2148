def sign(num):
    if type(num) != list:
        raise TypeError("not a list")
    x = 0
    for element in num:
        if element > 0:
            x += 1
    return x
sign([1, 2, 3, 4,5])
sign("1, 2, 3, 4, 5")

#labeling num as coexisting by a string name as well
#defined function to label if the numbers in the list are positive
  
