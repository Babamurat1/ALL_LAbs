# Вычисляем корень по итерационной формуле Герона

def main ():
    num=get_data()  # Получаем число
    if  num==0:     # Если число рано на 0
        print('Результат :',0)
    elif num<0:     # Условие если число меньше нулья
        print('Неверное значение !')
    elif num>0:     # Если число больше нулья будет вычислятся
        print('Результат :',calculate(num))     # Вывод
####################################################################

# Получаем данные от пользователья
def get_data():
    try:
        number =float(input('Введите число : '))
    except Exception as error:
        print(error)
        exit()
    else:           # Если не было вызвано исключение
        return  number
###################################################################

# Функция вычисления
def calculate(number):
    result=None
    x=2         # Любое случайное число
    flag=True       # Чтрбы запускать цикл
    check=None
    while flag:
        check=result
        result =0.5*(x+(number/x))  # Вычисление по формуле Герона
        x=result
        if result==check:           # Если одно и то же результат
            flag=False              # Цикл остановится
    return result                   # Возвращаем результат
##################################################################
main()