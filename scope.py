a_var = 'global value'

def example_func():
    print("This function can see the global scope variable = ", a_var)

example_func()

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()

for a in range(5):
    if a == 4:
        print(a, '-> a in for-loop')
print(a, '-> a in global')
        