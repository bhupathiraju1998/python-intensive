def get_discount(amount):
    if amount < 500:
        print("5%")
    elif amount >= 500 and amount < 2500:
        print("10%")
    else:
        print("20%")
    # Complete this function


amount = int(input())
# Call the get_discount function
get_discount(amount)