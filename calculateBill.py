def calculate_bill(amount):
    if amount < 500 :
        result = ((amount*5)/100)
        final_result = amount - result
        print(final_result)
    elif amount >= 500 and amount < 2500 :
        result = ((amount*10)/100)
        final_result = amount - result
        print(final_result)
    elif amount > 2500 or amount == 2500:
        result = ((amount*20)/100)
        final_result = amount - result
        print(final_result)
        
    # Complete this function


amount = int(input())
# Call the calculate_bill function
calculate_bill(amount)