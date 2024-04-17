# We dont have a data base thats why we are taking an input from the user
while True:
    print("Welcome to Dream World Shopping Center")
    name = input("Please provide the Your name:").title()
    print("Welcome to Dream world :", name)
    Total = 0

    while True:
        productname = input("please put the name of your product:")
        quantity = float(input("How many you are taking today ?: "))
        price = float(input("please put the price of each product:"))
        Total += price * quantity
        answer = input("Do you want to add some more products?  (Yes/No)")
        if answer == "yes" or answer == "Yes":
            additionalproductname = input("Please put the name of additional iteam :")
            additionalproductquantity = float(input("How many you are taking ?:"))
            additionalproductprice = float(
                input("please put the price of your additional product:"))
            Total2 = Total + additionalproductprice * additionalproductquantity
            print("-" * 40)
            print(name)
            print("Please pay $", Total2)
            print("-" * 40)
            print("******Happy Shopping******")
            break
        elif answer == "no" or answer == "No":
            print("-" * 40)
            print(name)
            print("Please pay $", Total)
            print("-" * 40)
            print("******Happy Shopping******")
            break



      
    

                   












