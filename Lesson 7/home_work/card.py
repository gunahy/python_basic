import random

class Card:
    """  Карточка состоит из 3 строк и 9 рядов.
    В кажой строке по 5 чисел. В первом столбце могут быть числа от 1 до 10, 
    во втором - от 11 до 20 и т.д. Всего в карточке заполнено 15 случайных чисел
    в диапазоне от 1 до 90.
    Attributes:
        self.max_in_line = 5 - количество чисел в строке
        self.row = 3 - количество строк
        self.column = 9 - количество колонок
        self.max_num = 90 - верхняя граница диапазона чисел для карточки
        card_array = [] - массив чисел записаных в карточку
        
    """

    def __init__(self, player):
        self.max_in_line = 5
        self.row = 3
        self.column = 9
        self.max_num = 90
        self.player = player
        self.card_array = [[0, 0, 0] for i in range(self.column)] 

        # Создадим контейнер для выбора числе от 1 до 90
        contanier = [_ for _ in range(self.max_num)]

        # Заполним self.card_array значениями из списка contanier, с условием
        # что в кажой строке должно быть не более 5 чисел
        for i in range(self.row):
            j = 0
            while j < self.max_in_line:
                rand_num = random.choice(contanier)
                get_column = (rand_num // 10) if rand_num >= 10 else 0
                if not self.card_array[get_column][i]:
                    self.card_array[get_column][i] = rand_num
                    contanier.pop(contanier.index(rand_num))
                else: # если число не 0, то необходимо откатить счетчик для повторной попытки
                    j -= 1
                j += 1


    def print_card(self):
        """ Выводим карточку в консоль """
        print('----------------------------')
        for i in range(self.row):
            for j in range(self.column):
                if self.card_array[j][i] < 10:
                    print('  ' + str(self.card_array[j][i]) if self.card_array[j][i] else '   ', end='')
                else:
                    print(' ' + str(self.card_array[j][i]) if self.card_array[j][i] else '  ', end='')
            print()
        print('----------------------------')


        
        
card = Card("Игрок")
print(card.card_array)
card.print_card()

