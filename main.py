class Animal():
    "Описание класса"
    voice = ""
    # конструктор (self~this в др ЯП)
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def __del__(self):
        print(self.__name,"удален из памяти")

    def make_voice(self):
        print(self.__name + " сказал " + self.voice)

class Elephant(Animal):
    voice = "уууу"

class Pig(Animal):
    voice = "хрю хрю"

print(Animal.__doc__)
lion = Animal("Лёва", 5)
print(lion.name + " сейчас " + str(lion.age) + " лет")
del lion

elephant = Elephant("Федя", -1) #инициализирую
print(elephant.age)
elephant.age = -5# но не присваиваю
print(elephant.name)
elephant.make_voice()

pig = Pig("Джордж", 3)
pig.make_voice()
