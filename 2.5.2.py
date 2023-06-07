a = int(input())
print(a//100)

class Meters:
    def __init__(self, string):
        self.string = string

    def from_string_to_number(self):
        if type(self.string) == str:
            numbers = int(self.string)
            return numbers

        elif type(self.string) == int:
            numbers = self.string
            return numbers
        else:
            print("Напишите число!")

    def convert_centimeters_to_meters(self):
        centimeters = self.from_string_to_number()
        return print(centimeters // 100)

    def convert_millimeters_to_meters(self):
        millimeters = self.from_string_to_number()
        return print(millimeters // 1000)


cm = Meters(input())
cm.convert_centimeters_to_meters()


# put your python code here
''' Distance in meters '''

def total_number_of_meters(number_of_centimeters):  # функция для расчёта полное число метров
    x = number_of_centimeters // 100
    print(x)

number_of_centimeters = int(input())  # ввод с клавиатуры число (целое)

total_number_of_meters(number_of_centimeters)  # вызов функции расчёта полное число метров