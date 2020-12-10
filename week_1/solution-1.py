
user_name = input("Enter Name: ")

def print_Diagonally(user_name):
    for i in range(len(user_name)):
        for j in range(len(user_name)):
            if i == j:
                print(user_name[i], end="")
            else:
                print(' ', end="")
        
        print('\n')


print_Diagonally(user_name)