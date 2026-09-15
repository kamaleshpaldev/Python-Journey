class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img

    def showNum(self):
        print(f"{self.real}i + {self.img}j")

    def addNum(self,n1):
        newReal= self.real+n1.real
        newImg = self.img+n1.img
        return Complex(newReal,newImg)


a =Complex(3,4)
b = Complex(5,6)
a.showNum()
b.showNum()
c = a.addNum(b)
c.showNum()