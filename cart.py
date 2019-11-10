from string import Template

class MyTemp(Template):
        delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="coke", price=8, qty=2))
    cart.append(dict(item="sprite", price=4, qty=1))
    cart.append(dict(item="cake", price=12, qty=1))

    t = MyTemp("#qty x #item = #price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
                
    print("Total: "+ str(total))

if __name__ == '__main__':
    Main()
