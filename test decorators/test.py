def bread(func):
    def wrapper():
        print("</------/>")
        func()
        print("</______/>")
    return wrapper
 
def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

@bread 
@ingredients
def sandwich(food="--курица--"):
    print(food)
 
#sandwich()
#выведет: --ветчина--
#sandwich = bread(ingredients(sandwich))
#sandwich()
#выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

sandwich()