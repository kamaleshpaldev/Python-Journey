class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,other):
        return self.price > other.price

o1=order("chips",35)
o2=order("chocolate",50)

print(o1>o2)