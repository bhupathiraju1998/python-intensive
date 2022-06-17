num = int(input())
thousand_note = 0
five_hundered_note = 0
hundered_note = 0
fifty_note = 0
twenty_note = 0
five_note = 0
one_note = 0
if num >= 1000:
    thousand_note = num // 1000
    num = num % 1000
if num >= 500:
    five_hundered_note = num // 500
    num = num % 500
if num >= 100:
    hundered_note = num // 100
    num = num % 100
if num >= 50:
    fifty_note = num // 50
    num = num % 50
if num >= 20:
    twenty_note = num // 20
    num = num % 20
if num >= 5:
    five_note = num // 5
    num = num % 5
if num >= 1:
    one_note= num // 1
    num = num % 1

print("1000:" + str(thousand_note))
print("500:" + str(five_hundered_note))
print("100:" + str(hundered_note))
print("50:" + str(fifty_note))
print("20:" + str(twenty_note))
print("5:" + str(five_note))
print("1:" + str(one_note))


