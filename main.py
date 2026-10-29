#Create a class reverse that consists of a constructor with a default value of string s.
#Then, create a method that will return the reversed string. 
#The value of string s must be equal to the word taken as input from the user.
class Reverse:
    def __init__(self, s = ""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

user_input = input("Enter a string to reverse: ").strip()
reverse_instance = Reverse(user_input)
reversed_string = reverse_instance.reverse_string()
print("Reversed string:", reversed_string)
