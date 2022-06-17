word_1 = input()
word_2 = input()
if word_1 == "Paper" and word_2 == "Scissors":
    print("Anjali Wins")
elif word_1 == "Paper" and word_2 == "Rock":
    print("Abhinav Wins")
elif word_1 == "Scissors" and word_2 == "Paper":
    print("Abhinav Wins")
elif word_1 == "Scissors" and word_2 =="Rock":
    print("Anjali Wins")
elif word_1 == "Rock" and word_2 == "Paper":
    print("Anjali Wins")
elif word_1 == "Rock" and word_2 == "Scissors":
    print("Abhinav Wins")
elif word_1 == "Rock" or "Paper" or "Scissors"  and word_2 == "Rock" or "Paper" or "Scissors":
    print("Tie")




