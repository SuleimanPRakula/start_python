def calc(x, y):
    return x + y

def render(x, y):
    print(x, y)

def pow(x, y):
    return x ** y

def wrap_calc(func):
    def result_func(x,y):
        x = x ** 2
        y = y ** 2

        return func(x, y)
 
    return result_func

if __name__ == '__main__':
    ready_func = wrap_calc(calc)

    print(render(4, 5))
    print(ready_func(4, 5))

