class OOP:
    
    def __init__(self):
        self._x = 'hi'

    def hello(self):
        print(f'{self._x}')
    
    def credit_calc(self):
        self._c = 1000+300+3
        return self._c
    
    def get_data(self):
        return f'Финальная сумма кредита {self._c}'
    
    x = property(hello, credit_calc, get_data)
    
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.credit_calc
    def x(self):
        return self._x

    @x.get_data
    def x(self):
        return self._x

