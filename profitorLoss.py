cp = int(input())
sp = int(input())
diff = sp - cp 
if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit - No Loss")