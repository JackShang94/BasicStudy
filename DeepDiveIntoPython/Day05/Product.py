class Product:
    # constructor
    '''
    （1）、__init__方法的第一参数永远是self，表示创建的类实例本身，
    因此，在__init__方法内部，就可以把各种属性绑定到self，
    因为self就指向创建的实例本身。
    （2）、有了__init__方法，在创建实例的时候，就不能传入空的参数了，
    必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去：
    '''
    def __init__(self, code, name, price): 
        self.code = code
        self.name = name
        self.price = price

    def calculate_gst(self):
        return self.price * 0.07

    def __repr__(self):
        return "Product('{}', '{}',{:.2f})".format(self.code, self.name, self.price)
