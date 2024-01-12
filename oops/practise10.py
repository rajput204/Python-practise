#outer and inner class
class course:
    def __init__(self,cn,cd,*books):
        self.cn=cn
        self.cd=cd
        self.books=[e for e in books]
    def showdetails(self):
        print(self.cn)
        print(self.cd)
        print('suggested books:-')
        for b in self.books:
            print(b)

    class books:
        def __init__(self,title):
            self.title=title
        def __str__(self):
            return self.title
c=course('python',10,'lean_python','python crash course')
c.showdetails()