def update_stock(l_d, l_id, quantity):
    # Retrieve the furniture information using the provided ID
    Furniture_info = l_d[l_id]

    # Ensure the stock quantity is correctly indexed (assuming it's the 3rd element)
    stock = int(Furniture_info[2])  # Adjust index if necessary
    new_stock = stock - quantity

    # Update the stock in the Furniture_info list
    Furniture_info[2] = str(new_stock)

    # Automatically reorder if stock drops below 10
    if new_stock < 10:
        reorder_amount = 20
        Furniture_info[2] = str(new_stock + reorder_amount)
        print(f"Stock for {Furniture_info[1]} was low. Reordered {reorder_amount} units.")

    # Update the file with new stock information
    with open("furniture.txt", "w") as f:
        for key, value in l_d.items():
            # Join the furniture details with commas
            f.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")
