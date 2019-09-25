class Product:
    # constructor
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def calculate_gst(self):
        return self.price * 0.07

    def __repr__(self):
        return "Product('{}', '{}',{:.2f})".format(self.code, self.name, self.price)
