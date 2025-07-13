def read_Furniture():
    furniture_dict = {}
    with open("furniture.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            # Assuming the order is: Manufacturer, Name, Quantity, Price
            furniture_dict[len(furniture_dict) + 1] = data
    return furniture_dict


















