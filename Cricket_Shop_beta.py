import pyfiglet

def cricket_shop():
    cart = {}
    Total_Cost = 0
    while True:
        try:
            # Displays title
            title = "Cricket Goods 1.0"
            title_big = pyfiglet.figlet_format(title, font="standard")
            print(title_big)

            # Displays subheading
            sub_heading = "Best Cricket Shop"
            sub_heading_big = pyfiglet.figlet_format(sub_heading, font="standard")
            print(sub_heading_big)

            # Item list
            equipments = { 
                1: ("Leather Ball", 10),
                2: ("Cricket Bat", 75),
                3: ("Cricket Gloves", 20),
                4: ("Cricket Pads", 50),
                5: ("Cricket Helmet", 50),
                6: ("Arm Guard", 20),
                7: ("Thigh Pad", 20),
                8: ("Full Cricket Kit", 225),
            }

            # Display equipment
            for key, (equipmentName, Cost) in equipments.items():
                print(f"{key}. {equipmentName}; Price: {Cost}")

            print("\nEnter 0 to exit the shop\n")
            Desired_Item = int(input("Enter number of desired item:"))
            
            if Desired_Item == 0:
                print("Thank you for visiting Cricket Goods 1.0! Goodbye!")
                break  # Exits loop

            if Desired_Item not in equipments:
                print("Invalid user input! Try again!")
                continue  # Restarts the loop if input is invalid

            Number_ofItems = int(input("Enter how many of the same item wanted:"))
            if Number_ofItems < 1:
                print("Enter a valid QUANTITY!")
                continue  # Restarts loop if quantity is invalid

            # Get the equipment and its cost from the dictionary
            equipmentName, equipmentCost = equipments[Desired_Item]

            # Update the cart with the new item or update the quantity if it already exists
            if equipmentName in cart:
                cart[equipmentName] = (
                    cart[equipmentName][0] + Number_ofItems,  # Update quantity
                    cart[equipmentName][1] + (equipmentCost * Number_ofItems)  # Update total cost
                )
            else:
                cart[equipmentName] = (Number_ofItems, equipmentCost * Number_ofItems)  # New item added to cart

            # Update the total cost
            Total_Cost += equipmentCost * Number_ofItems
            
            

            # Ask if the user wants to buy more items
            another_purchase = input("Would you like to buy another item? (yes/no): ").strip().lower()

            if another_purchase == "no":  # If the user types "no"
                # Show cart and total cost, then exit
                print("\nYour Cart:")
                for item, (qty, cost) in cart.items():
                    print(f"{item}: {qty} pcs, Total: ${cost}")
                print(f"Total Cost: ${Total_Cost}\n")
                print("Thank you for shopping at Cricket Goods 1.0! Have a great day!")
                break  # Exit the loop after displaying the final total and cart

            elif another_purchase == "yes":  # If the user types "yes"
                continue  # Continue the loop to allow more purchases

            else:  # If the user types anything other than "yes" or "no"
                print("Invalid Input! Please enter 'yes' or 'no'.")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")

cricket_shop() 
#trigger the build now

