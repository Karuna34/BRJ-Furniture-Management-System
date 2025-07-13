import operation
from read import read_Furniture

def main():
    print("\n------------------------------------\n")
    print("\n| Welcome to BRJ Furniture Store |\n")
    print("\n------------------------------------\n") 

    continueOptions = True
    while continueOptions:
        print("SELECT A DESIRED OPTION :\n")
        print("\n---------------------------------\n")
        print(" Enter 1 to Purchase Furniture")
        print(" Enter 2 to Sell Furniture ")
        print(" Enter 3 to Exit")
        print("\n---------------------------------\n")

        try:
            user_input = int(input("Enter a number :"))
            if user_input == 1:
                print("\n----------------------------------------\n")
                print("\n| Purchase Furniture Details |\n")
                print("\n----------------------------------------\n")
                
                # Load furniture data (as dictionary)
                l_d = read_Furniture()  # Ensure this returns a dictionary with furniture data
                
                # Call make_purchase() with l_d passed as argument
                operation.make_purchase(l_d)
            
            elif user_input == 2:
                print("\n----------------------------------------\n")
                print("\n| Sell Furniture Details |\n")
                print("\n----------------------------------------\n")
                
                # Load furniture data (as dictionary)
                l_d = read_Furniture()  # Ensure this returns a dictionary with furniture data
                
                # Call make_sale() with l_d passed as argument
                operation.make_sale(l_d)

            elif user_input == 3:
                print("\n----------------------------------------\n")
                print("\n| Thank you for your visit! Good Day |\n")
                print("\n----------------------------------------\n")
                break

            else:
                print("\n Invalid Input \n")
                
        
        except ValueError:
            print("please enter a valid option")

main()
