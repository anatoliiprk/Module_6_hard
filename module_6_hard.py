import math

print('------\nЗадание "Они все так похожи"\n------')


class Figure:
    def __init__(self, __sides: list, __color: tuple, filled=True):
        self.filled = filled
        self.__color = __color
        self.sides_count = 0



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        check = self.__is_valid_color(r, g, b)
        if check:
            self.__color = (r, g, b)
        return self.__color

    def __is_valid_sides(self, *sides):
        flag1 = False
        count = 0
        for side in sides:
            if isinstance(side, int) and side > 0:
                flag1 = True
                count += 1
            else:
                flag1 = False
                break
        if flag1 and count == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        sides = self.__sides
        return sides

    def __len__(self):
        summa = sum(self.__sides)
        return summa

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if len(new_sides) == self.sides_count or (self.sides_count == 12 and len(new_sides) == 1):
            self.__sides = new_sides
        return self.__sides


class Circle(Figure):
    def __init__(self, __sides, __color, filled=True):
        Figure.__init__(self, __sides, __color, filled=True)
        self.sides_count = 1
        self.__color = __color
        self.filled = filled
        if self.sides_count == len(__sides):
            self.__sides = __sides
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
        self.__radius = self.__sides[0] / (2 * math.pi)


    def get_square(self):
        S = math.pi * (self.__radius ** 2)
        return S


class Triangle(Figure):
    def __init__(self, __sides, __color, filled=True):
        Figure.__init__(self, __sides, __color, filled=True)
        self.sides_count = 3
        self.__color = __color
        self.filled = filled
        if self.sides_count == len(__sides):
            self.__sides = __sides
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)


    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        S = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
        return S


class Cube(Figure):
    def __init__(self, __sides, __color, filled=True):
        Figure.__init__(self, __sides, __color, filled=True)
        self.sides_count = 12
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

        if len(self.__sides) == 1:
            side = self.__sides[0]
        else:
            side = 1
        for i in range(11):
            self.__sides.append(side)
            i += 1

    def get_volume(self):
        V = self.__sides[0] ** 3


#------
circle1 = Circle([10], (200, 200, 100))
print(circle1.get_color())
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle1.set_sides(15)
print(circle1.get_sides())
print('------')

cube1 = Cube([6], (100, 100, 50))
print(cube1.get_color())
cube1.set_sides(10)
print(cube1.get_sides())
print('------')

triangle1 = Triangle([3, 4, 5], (250, 250, 150))
print(triangle1.get_color())
triangle1.set_sides(1, 2, 3)
print(triangle1.get_sides())
print('------')