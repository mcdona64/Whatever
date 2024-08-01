
class Whatever:

    def __getattr__(self, item):
        return self

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __repr__(self):
        return 'Whatever'
    
    def __str__(self):
        return 'Whatever'

    def __instancecheck__(self, instance):
        return True

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __mul__(self, other):
        return self

    def __divmod__(self, other):
        return self

    def __floordiv__(self, other):
        return self

    def __truediv__(self, other):
        return self

    def __mod__(self, other):
        return self

    def __pow__(self, power, modulo=None):
        return self
