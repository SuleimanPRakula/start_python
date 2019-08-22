
def wrap_calc(func):
    def result_func(x,y):
        x = x ** 2
        y = y ** 2

        return func(x, y)
 
    return result_func

def wrap_message(func):
    def result_func():
        print('от Директора')
        func()
        print('С наилучшими пожеланиями, Спасибо что написали')
    
    return result_func