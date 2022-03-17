from Product import Product

def init_product_list(p_list):
    p = Product('1001', 'Apple iPhone', 1088.00)
    p_list.append(p)
    p = Product('1005', 'HTC Desire', 888.00)
    p_list.append(p)
    p = Product('1013', 'LG Optimus', 788.00)
    p_list.append(p)
    p = Product('1022', 'Sony Xperia', 958.00)
    p_list.append(p)
    p = Product('1027', 'Samsung Galaxy', 988.00)
    p_list.append(p)


def list_products(p_list):
    print('{:<20}{:<20}{:<20}{:<20}'.format('Code', 'Name', 'Price', 'GST'))
    for p in p_list:
        print('{:<20}{:<20}${:<20.2f}${:<20.2f}'.format(p.code, p.name, p.price, p.calculate_gst()))


def list_products_below_target(p_list, target):
    print('{:6}{:20}{:8}'.format('Code', 'Name', 'Price'))
    for p in p_list:
        if p.price < target:
            print('{:6}{:20}{:8.2f}'.format(p.code, p.name, p.price))


product_list = []
init_product_list(product_list)

print('Displaying all the products')
list_products(product_list)

print()

target = float(input('Enter the target price: '))
print('Displaying the product below ${}'.format(target))
list_products_below_target(product_list, target)
