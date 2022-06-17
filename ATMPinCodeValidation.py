def validate_atm_pin_code(pin):
    result = True
    length = (len(pin) == 4) or (len(pin) == 6)
    if length:
        for each in pin:
            if  not each.isdigit():
                result = False
            
    else:
        result = False
    if result:
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")
    
    
    # Complete this function


pin = input()
# Call the validate_atm_pin_code function
validate_atm_pin_code(pin)