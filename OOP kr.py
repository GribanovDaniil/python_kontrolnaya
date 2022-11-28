# -*- coding: windows-1251 -*-


'''Класс Воздушный Замок (AirCastle) Экземпляр класса инициализируется
   с аргументами: высота; - количество состовляющих облаков; - цвет.
   Класс должен реализовывать методы: - change_height(value), может
   уменьшиться только до нуля; - сложить с числом, добавляется n
   облаков к замку, одновременно увеличивается высота на n//5; -
   экземпляр класса можно вызвать с аргументов - целым числом,
   означающим 46 прозрачность облаков; метод возвращает значение
   видимости замка, рассчитанное по формуле: высота // прозрачность *
   количество облаков; __str__ - возвращает строковое представление в виде:
   The AirCastle at an altitude of meters is with clouds.
   - экземпляры можно сравнивать: сначала по количеству облаков,
   затем по высоте, затем по цвету, по алфавиту' для этого нужно
   реализовать методы сравнения: >,<.'''




class AirCastle():
    def __init__(self, height, clouds, color, transparency):
        self.height = height
        self.clouds = clouds
        self.color = color
        self.transparency = 46

    def change_height(self, value, n):
        self.height = value
        self.clouds += n
        value = value + (n // 5)

    def __str__():
        print("The AirCastle at an altitude of meters is with clouds")

    def visibility(height, transparency, clouds):
        return ((height // transparency) * clouds)

    def __gt__(self, other):
        return self > other

    def __lt__(self, other):
        return self < other

