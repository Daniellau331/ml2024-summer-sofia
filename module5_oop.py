'''
The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and 
reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and 
outputs: "-1" if there were no such X among N read numbers, or the 
index (from 1 to N) of this X if the user inputted it before.

The basic functionality of data processing (data initialization, data insertion, 
data search) should be done via Object-Oriented Programming Paradigm 
(i.e. using Classes)
'''
class Program():
    def __init__(self) -> None:
        self.dict = {}

    def get_number_size(self):
        n_size = input("Enter the size of N:\n")
        return n_size

    def get_input(self, n_size):
        for x in range(int(n_size)):
            n_input = input("Enter numbers in N:\n")
            self.dict[n_input] = x

    def verify_data(self,n_size):
        for x in range(int(n_size)):
            x_input = input("Enter numbers in X:\n")
            if x_input in self.dict:
                # print("index of this number is: "+str(x))
                print("index of this number is: "+ str(self.dict[x_input]+1))
            else:
                print(-1)

program = Program()
n = program.get_number_size()
program.get_input(n)
program.verify_data(n)
