#Update the Student Class to include these attributes - first_name, last_name, age, country- Add these methods to the Student class
#- show_full_name__
# year_of_birt show_initials
class student:
    first_name = "yvonne"
    last_name ="atieno"
    age=24
    country ="Kenyan"
    def __init__(self, first_name, last_name, age, country):        
     self.first_name=first_name
     self.last_name=last_name
     self.age=age
     self.county=country
    def show_full_name(self):
       return f"{self.first_name} {self.last_name}" 
    def year_of_birth(self):
       return f"{self}"
    








    





      
        
        
    

    
