import random
import matplotlib.pyplot as plt
import numpy as np

# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

# Задача 2. Имеются данные о площади и стоимости 15 домов.Риелтору требуется узнать в каких домах стоимость
#  квадратного метра меньше 50000 рублей. Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов,
#  отсортированных по площади. Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

def function():
    x_list =[]
    y_list = []
    for x in range(-10,11):
        y = 5*x**2 + 10*x - 30
        x_list.append(x)
        y_list.append(y)
    
    plt.axhline(y = 0,color= 'r', linestyle = 'dotted')
    plt.plot(y_list)
    plt.show()
# function()

def house():
        
    size = 15
    houses = np.random.randint(100,300, size)
    price = np.random.randint(3000000, 20000000, size)
    mean_pr = [round(price[i]/houses[i]) for i in range(len(price))]
    print(mean_pr)

    names = ['дом 1',
            'дом 2',
            'дом 3',
            'дом 4',
            'дом 5',
            'дом 6',
            'дом 7',
            'дом 8',
            'дом 9',
            'дом 10',
            'дом 11',
            'дом 12',
            'дом 13',
            'дом 14',
            'дом 15']

    plt.axhline(y = 50000,color= 'b', linestyle = 'dotted')
    # plt.plot(mean_pr, 'ro')
    plt.bar(names,mean_pr)

    plt.show()


house()        
