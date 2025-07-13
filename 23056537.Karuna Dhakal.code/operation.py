import datetime
import random
from read import read_Furniture
from write import update_stock

# Purchase furniture
def make_purchase(l_d):
    # Collect customer details with validation
    name = input("Enter your name: ").strip()
    while not name:
        print("ALERT! Name is required.")
        name = input("Enter your name: ").strip()

    phone_number = input("Enter your phone number: ").strip()
    while not phone_number:
        print("ALERT! Phone number can't be empty.")
        phone_number = input("Enter your phone number: ").strip()

    # Display available furniture
    print("\n------------------------------------\n")
    print("| Available Furniture in Stock |\n")
    print("------------------------------------\n")
    for Furniture_id, Furniture_info in l_d.items():
        if len(Furniture_info) == 4:  # Ensure proper data
            print(f"{Furniture_id}\t{Furniture_info[0]}\t{Furniture_info[1]}\t{Furniture_info[2]}\t${Furniture_info[3]}")
        else:
            print(f"Error: Data for Furniture ID {Furniture_id} is incomplete.")

    # Process user selections
    selected_items = []
    while True:
        try:
            l_id = int(input("Enter the Furniture ID (or 0 to finish selection): ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid Furniture ID.")
            continue

        if l_id == 0:
            if selected_items:
                print("Thank you!")  # Successful selection completion
                break
            else:
                print("You haven't selected any items yet.")
                continue

        if l_id not in l_d:
            print("Invalid ID. Please try again.")
            continue

        # Get quantity
        try:
            quantity = int(input("Enter the quantity: ").strip())
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if quantity > int(l_d[l_id][2]):
            print(f"Sorry, only {l_d[l_id][2]} items are available in stock.")
            continue

        # Add selected item to the list
        selected_items.append((l_id, quantity))
        # Update stock
        l_d[l_id][2] = str(int(l_d[l_id][2]) - quantity)

    # Calculate total amount with discount and shipping
    total_amount = sum(float(l_d[item[0]][3].replace("$", "").strip()) * item[1] for item in selected_items)
    discount = total_amount * 0.1 if total_amount > 1000 else 0
    total_amount -= discount

    # Add shipping cost
    shipping_cost = 50.0 if total_amount < 500 else 0.0
    total_amount += shipping_cost

    # Generate bill
    bill_number = random.randint(0, 99999)
    file_name = f"{name}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"

    with open(file_name, 'w') as file:
        file.write("-------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t Furniture Purchase Invoice\n")
        file.write("-------------------------------------------------------------------------------\n")
        file.write(f"Bill Number: {bill_number}\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Date and Time of Purchase: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write("Itemized Details:\n")
        for item in selected_items:
            file.write(f"Furniture Name: {l_d[item[0]][1]}, Quantity: {item[1]}, Price: {l_d[item[0]][3]}\n")

        file.write(f"\nDiscount: ${discount:.2f}\n")
        file.write(f"Shipping Cost: ${shipping_cost}\n")
        file.write(f"Total Amount: ${total_amount:.2f}\n")
        file.write("\n\nThank you for your purchase, Visit again ☺ !\n")
        file.write("-------------------------------------------------------------------------------\n")

    print(f"Purchase Invoice has been generated and saved as {file_name}")
    
    # Update stock after purchase and write to file
    update_stock(l_d)
    print("\n")


# Sell furniture
def make_sale(l_d):
    print("\n----------------------------------------\n")
    print("\n| Sell Furniture Details  |\n")
    print("\n----------------------------------------\n")

    print("--------------------------------------------------------------------------------------------------")
    print("ID\tFurniture Name\t Manufacturer Name\tPrice\tQuantity Available\tLocation\tType")
    print("--------------------------------------------------------------------------------------------------")
    
    for Furniture_id, Furniture_info in l_d.items():
        if len(Furniture_info) == 4:
            print(Furniture_id, end="\t")
            print("\t".join(Furniture_info))
        else:
            print(f"Error: Data for Furniture ID {Furniture_id} is incomplete.")
    
    print("--------------------------------------------------------------------------------------------------")
    print("\n")
    
    Furniture_id = int(input("Enter the ID of the Furniture you want to buy: "))
    Furniture_info = l_d.get(Furniture_id)
    
    if Furniture_info and len(Furniture_info) == 4:
        name = input("Enter name of the customer: ")
        phone_number = input("Enter phone number of the customer: ")
        quantity = int(input("Enter quantity of Furniture you want to buy: "))
        
        if quantity > int(Furniture_info[2]):
            print(f"Sorry, only {Furniture_info[2]} items are available.")
            return
        
        # Update stock
        Furniture_info[2] = str(int(Furniture_info[2]) - quantity)

        # Calculate total cost
        cost = float(Furniture_info[3].replace("$", "").strip())
        total_amount = cost * quantity

        # Apply discount for bulk purchase
        discount = total_amount * 0.05 if quantity >= 5 else 0
        total_amount -= discount

        shipping_cost = 100.0 if quantity < 5 else 50.0
        total_amount += shipping_cost

        # Generate and write invoice
        file_name = name + "-" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"
        
        with open(file_name, 'w') as file:
            file.write("--------------------------------------------------------------\n")
            file.write("\t\t\t Furniture Sale Invoice\n")
            file.write("--------------------------------------------------------------\n")
            file.write(f"Customer Name: {name}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Date and Time of Purchase: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("\n\n")
            file.write(f"Total Amount: ${total_amount - shipping_cost:.2f}\n")
            file.write(f"Discount Applied: ${discount:.2f}\n")
            file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
            file.write(f"Final Amount: ${total_amount:.2f}\n")
            file.write("----------------------------------------------------\n")

        print(f"Invoice generated and saved as {file_name}")
        
        # Update stock after sale
        update_stock(l_d, Furniture_id, quantity)
        print("\n")

    else:
        print("Error: Invalid Furniture ID or incomplete data.")


