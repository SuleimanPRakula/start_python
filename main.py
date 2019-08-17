from wrap import wrap_calc



@wrap_calc
def calc(x, y):
    return x + y

@wrap_calc
def render(x, y):
    print(x, y)

@wrap_calc
def pow(x, y):
    return x ** y

if __name__ == '__main__':
    print(calc(4,5))
