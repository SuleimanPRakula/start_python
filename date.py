from datetime import datetime as d

def current_date(func):
    def result_func(text):
        print(text)
        #выводим текст оборачиваемой функции
        rudate=d.today().strftime("%d.%m.%Y")
        #конвертируем дату в читаемый формат
        print(rudate)
        #выводим дату следующей строкой после текста
    
    return result_func