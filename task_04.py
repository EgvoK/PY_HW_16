#### TASK 04 ####
# Создайте приложение по выпечке пиццы.
# Каждая пицца содержит разные компоненты.
# Используя механизм декораторов создайте разные пиццы:
# - Маргарита;
# - Четыре сыра;
# - Капричоза;
# - Гавайская.

def selector(func):
    def wrapper():
        print("-" * 100)
        func()
    return wrapper


def dough(func):
    def wrapper():
        func()
        print("dough")
    return wrapper


def tomatoSauce(func):
    def wrapper():
        func()
        print("tomato sauce")
    return wrapper


def mozzarella(func):
    def wrapper():
        func()
        print("mozzarella")
    return wrapper


def tomatoes(func):
    def wrapper():
        func()
        print("tomatoes")
    return wrapper


def basil(func):
    def wrapper():
        func()
        print("basil")
    return wrapper


def oliveOil(func):
    def wrapper():
        func()
        print("olive oil")
    return wrapper


def emmental(func):
    def wrapper():
        func()
        print("emmental")
    return wrapper


def gorgonzola(func):
    def wrapper():
        func()
        print("gorgonzola")
    return wrapper


def parmesan(func):
    def wrapper():
        func()
        print("parmesan")
    return wrapper()


def driedOregano(func):
    def wrapper():
        func()
        print("dried oregano")
    return wrapper


def mushrooms(func):
    def wrapper():
        func()
        print("mushrooms")
    return wrapper


def olives(func):
    def wrapper():
        func()
        print("olives")
    return wrapper


def ham(func):
    def wrapper():
        func()
        print("ham")
    return wrapper


def pineapples(func):
    def wrapper():
        func()
        print("pineapples")
    return wrapper


@selector
@oliveOil
@basil
@tomatoes
@mozzarella
@tomatoSauce
@dough
def getMargaritaPizzaIngredients():
    print("Margarita pizza ingredients:")


@selector
@driedOregano
@parmesan
@gorgonzola
@emmental
@mozzarella
@dough
def getFourCheesesPizzaIngredients():
    print("Four Cheeses pizza ingredients:")


@selector
@basil
@ham
@olives
@mushrooms
@mozzarella
@tomatoSauce
@dough
def getCaprichosaPizzaIngredients():
    print("Caprichosa pizza ingredients:")


@selector
@mozzarella
@pineapples
@ham
@driedOregano
@tomatoSauce
@dough
def getHawaiianPizzaIngredients():
    print("Hawaiian pizza ingredients:")


getMargaritaPizzaIngredients()
getCaprichosaPizzaIngredients()
getHawaiianPizzaIngredients()
