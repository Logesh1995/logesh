class val:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def get_user_input(self):

        a = int(input('Enter side a:'))
        b = int(input('Enter side b:'))
        c = int(input('Enter side c:'))
        return self(a, b, c)
class area(val):

    def __init__(self, *args):
        super(area, self).__init__(*args)
    def cal(self):
        s = (self.a + self.b + self.c)*0.5
        ar = (s*(s - self.a)*(s - self.b)*(s - self.c))**0.5
        return ar


a1 = area.get_user_input()
ar1 = a1.cal()
print(ar1)







