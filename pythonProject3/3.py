def outer_fun(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5

rs = outer_fun(5, 10)
print(rs)