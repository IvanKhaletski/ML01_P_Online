<<<<<<< HEAD

# Здесь мы задаем наше главное уравнение для расчета расхода топлива на заданную дистанцию (из обыкновенной пропорции)
# L - длина маршрута, которую нужно будет задать вречную
# V - расход топлива на 100 км, которыей такхи задается вручную
# V1 - общий расход топлива, который будет расчитак по формуле
def function(L, V):
    return (L*V) / 100

def main(): # определяем основную функцию main, где будет происходить выполнение программы
    try: # конструкция try используется для определения блока, в кот. могут быть искл-я
        L = float(input("Введите длину маршрута в километрах: ")) ##ввод значения с клавы
        if L <= 0: #условие
            raise ValueError("Длина маршрута должна быть больше 0.") ## отлов ошибки с неверным значением
=======
def function(L, V):
    return (L*V) / 100

def main():
    try:
        L = float(input("Введите длину маршрута в километрах: "))
        if L <= 0:
            raise ValueError("Длина маршрута должна быть больше 0.")
>>>>>>> 282f9c2e7ad98124abd2f8e8f617d06ab1caaeef

        V = float(input("Введите расход топлива на 100 километров: "))
        if V <= 0:
            raise ValueError("Расход топлива должен быть больше 0.")

<<<<<<< HEAD
        V1 = function(L, V) # расчет общего расхода топлива по формуле, кот. мы задали выше
        print(f"Общий расход топлива на маршруте составит: {V1:.2f} литров.")

    except ValueError as e: # эта конструкция позволяет отлавливать все возможные ошибки кроме ValueError. 
        # но вначале мы выделили класс обшибок ValueError, т.к. хотим, чтобы юзеру высвечивался тест с этой ошибкой 
=======
        V1 = function(L, V)
        print(f"Общий расход топлива на маршруте составит: {V1:.2f} литров.")

    except ValueError as e:
>>>>>>> 282f9c2e7ad98124abd2f8e8f617d06ab1caaeef
        print(f"Ошибка ввода: {e}")
if __name__ == "__main__":
    main()