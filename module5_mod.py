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