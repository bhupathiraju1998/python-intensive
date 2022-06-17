attendance = input()
medical_reason = input()

length = len(attendance)

attendance = attendance[:(length-1)]
attendance = int(attendance)

if attendance >= 75:
    print("Allowed to write exam")

elif attendance < 75 and medical_reason == "Y":
    print("Allowed to write exam")

else:
    print("Cannot write exam")
