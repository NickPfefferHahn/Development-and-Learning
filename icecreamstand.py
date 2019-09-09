class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Welcome to the " + self.restaurant_name.title() + ".")
        print("Our cuisine consists of: " + self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        print("Welcome, " + self.restaurant_name.title() + " is OPEN!")

# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, flavors = ['']):
        self.flavors = flavors
       
    def show_flavors(self):
        print("These are our flavors: " + str(self.flavors))

show_icecream = IceCreamStand(['Vinilla', 'chocolate', 'peanutbutter', 'strawberry'])
show_icecream.show_flavors()





        
    