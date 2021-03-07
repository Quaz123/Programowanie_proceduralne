list_of_functions = []

# przykładowy dekorator
def recorder(f):
    print('użyto funkcji %s' % f)
    list_of_functions.append(f)
    return f

# dekorowanie funkcji f_sum - sposób I
@recorder
def f_sum(a, b):
    return a + b

def f_product(a, b):
    return a * b

# dekorowanie funkcji f_product - sposób II
f_product = recorder(f_product)

def f_difference(a, b):
    return a - b

print("zarejestrowane funkcje: ->", list_of_functions)

print(f_sum(1,3))
print(f_product(7,8))
print(f_difference(7,8))

print("zarejestrowane funkcje: ->", list_of_functions)
