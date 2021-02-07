# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т



print("\nFind the mass of asphalt for the road in 5 centimeter\n")

class Road:
    def __init__(self, _lenth, _width):
        self._length = _lenth
        self._width = _width

    def mas(self, thickness):
        square_count = self._length * self._width
        return thickness * 25 * square_count

if __name__ == '__main__':
    a = Road(int(input("Input length: \n")), int(input("Input width:\n")))
    print(f"{a.mas(5)} kg")