class A:
    def className(self):
        print("class A")

class B:
    def className(self):
        print("class B")

class C(A,B):
    def className(self):
        super().className() 
        print("call from class C")

class D(B,A):
    def className(self):
        super().className()
        print("call from class D")


object1 = C()
object1.className()

print('..........................')

object2 = D()
object2.className()
