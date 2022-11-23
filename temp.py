from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number):
    '''Вычисляет квадратный корень.     '''
    x = sqrt(number)
    return x


def calc(your_number):
    '''Рассчитывает квадратный корень.'''
    root = CalculateSquareRoot(your_number)
    if your_number >= 0:
        return root
    else:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {root}')


calc(25.5)
