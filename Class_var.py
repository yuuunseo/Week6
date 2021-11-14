class Class_var:

    def __init__(self, first, second):
        self.ten = 10
        self.twenty= 20

    def print_self_var(self):
        print(self.ten,self.twenty,sep=' ')

    def function1(self):
        result1 = self.ten * 10
        result2 = self.twenty * 10
        '''return result1, result2'''
        print(result1,result2,sep=' ')
