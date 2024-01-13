#polymorphism

class english:
    def greeting(self):
        print("hello")
class french:
    def greeting(self):
        print("bonjour")
def greet(language):
    language.greeting
e=english()
e.greeting()
f=french()
f.greeting()