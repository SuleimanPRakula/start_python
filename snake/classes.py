class Snake:
    def __init__(self, length):
        self.__length = length
        self.__position = 0
    def crawl(self):
        self.__position += 10
        return self.__position

    def hiss(self):
        print('ssss...')

    def detect_enemy(self,snake):
        try:
            snake.crawl()
            snake.hiss()

            print('Ok :)')
            return False

        except:
            print('SSSSS!!! >.<')
            return True
    
    @property
    def position(self):
        return self.__position

    @property
    def length(self):
        return self.__length

class Ninja(Snake):
    pass