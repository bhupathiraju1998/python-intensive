def get_speed_status(speed):
    if speed < 60:
        print("Normal")
    elif speed >= 60 and speed < 80:
        print("Warning")
    else:
        print("Over Speed")


speed = int(input())
# Call the get_speed_status function
get_speed_status(speed)