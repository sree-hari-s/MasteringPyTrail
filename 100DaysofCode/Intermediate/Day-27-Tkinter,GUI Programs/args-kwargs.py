"""
unlimited
args - arguments
* operator collects all the arguments into a tuple
"""
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3, 4)


"""
unlimited keyword arguments
kwargs - keyword arguments
** operator make it a dictionary
"""

def calculate(n,**kwargs):
    print(kwargs)
    # for key , value in kwargs.items():
    #     print(key, value)
    n+= kwargs['add']
    n*= kwargs['multiply']
    print(n)
    
calculate(2,add=3,multiply=5)

class Car:
    
    def __init__(self , **kw):
        """
        self.model = kw['model'] instead of using this if we use get 
        even if we do not provide it while initializing we wont get an error
        """
        self.model = kw.get('model')
        self.brand = kw.get('brand')
        self.price = kw.get('price')
        self.seats = kw.get('seats') 
