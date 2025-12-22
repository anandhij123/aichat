"""What is a Class and Object?  
- Class: A blueprint for creating objects  
- Object: An instance of a class"""
class Car:
    def __init__(self, model, cartype, color):
     self.model = model
     self.cartype = cartype
     self.color = color

    def fav_display(self):
      print( "Favorite car:"+self.model+" "+self.cartype+" "+self.color)

tata = Car("punch","Electric","Silver")
tata.fav_display()
audi = Car("Audi A4","Automatic", "Blue")
ferrari = Car("Ferrari 488","Electric", "Green")
audi.fav_display()
ferrari.fav_display()
