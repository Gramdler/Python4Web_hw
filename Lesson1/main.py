class Meta(type):
    # тут должно быть ваше решение
    #children_number = 0
    def __new__(cls, name, *args, **kwargs):
        x = super().__new__(cls, name, *args,**kwargs)
        x.class_number = Meta.children_number
        Meta.children_number += 1
        return x

Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

class Cls3(metaclass=Meta):
    def __init__(self, data):
        self.data = data

if __name__ == '__main__':

    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
    c = Cls3('')
    print(c.class_number)



