from wrap import wrap_calc, wrap_message
from date import current_date as today_date


@wrap_calc
def calc(x, y):
    return x + y

@wrap_calc
def render(x, y):
    print(x, y)

@wrap_calc
def pow(x, y):
    return x ** y

@today_date
@wrap_message
def message(text='Здравствуйте, это декораторы'):
    print(text)

if __name__ == '__main__':
    print(calc(4,5))

    message()
    
