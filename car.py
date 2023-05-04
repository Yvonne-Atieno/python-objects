#Car
class car:
    name="Mazda"
    model="camry"
    colour="white"
    def __init__(self,name,model,colour):
        self.name=name
        self.model=model
        self.colour=colour
    def greet_student(self):
        return f"I need{self.name},{self.model}which is{self.colour}"
        