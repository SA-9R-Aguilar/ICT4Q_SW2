class Classmate:
    def __init__(self, name, section, type, favorite_subject):
        self.name = name
        self.section = section
        self.type = type
        self.favorite_subject = favorite_subject
    def introduce(self):
        print(f"{self.name} from {self.section} is a {self.type} who loves {self.favorite_subject}.")

classmate1 = Classmate("Cinnamoroll", "Sanrio", "white puppy", "Cinnamon rolls") 
classmate1.introduce()

classmate2 = Classmate("Arianne", "Ruby", "female student", "Chemistry")
classmate2.introduce() 

classmate3 = Classmate("Caleb", "Ruby", "male student", "Social Studies")
classmate3.introduce()

classmate4 = Classmate("Jacob", "Ruby", "male student", "Cars") 
classmate4.introduce()

classmate5 = Classmate("Ms. Onofre", "Emerald", "Teacher", "ICT") 
classmate5.introduce()
