def main():
    num = calculate(add=3, multiply=5)
    # print(num)

    class Car:
        def __init__(self, **kw):
            self.make = kw['make']
            self.model = kw.get('model') # this way stops the program from crashing if there is no argument for 'Model'

    my_car = Car(make='Honda')
    print(my_car.model)

def add(*args):
    num = 0

    for arg in args:
        num += arg

    return num

def calculate(**kwargs):
    n = 10

    # for k,v in kwargs.items():
    #     print(k)
    #     print(v)

    n *= kwargs['multiply']
    n += kwargs['add']

    return n


main()