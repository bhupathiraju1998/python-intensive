num = int(input())

dictonary = {
}
    
count1 = 0
count2 = 0
for each in range(num):
    given_each_match = input().split(";")
    if given_each_match[0] in dictonary:
        pass
    else:
        dictonary[given_each_match[0]] = {"win":0,"draw":0,"loss":0,"points":0}
    if given_each_match[1] in dictonary:
        pass
    else:
        dictonary[given_each_match[1]] = {"win":0,"draw":0,"loss":0,"points":0}
    if given_each_match[2] == "draw":
        team1 = given_each_match[0] 
        team2 = given_each_match[1]
        draw = "draw"
        dictonary[team1][draw] +=  1
        dictonary[team2][draw] +=  1
            
    if given_each_match[2] == "win":
        team1 = given_each_match[0]
        team2 = given_each_match[1]
        win = "win"
        loss = "loss"
        dictonary[team1][win] +=  1
        dictonary[team2][loss] +=  1
    if given_each_match[2] == "loss":
        team1 = given_each_match[0] 
        team2 = given_each_match[1]
        win = "win"
        loss="loss"
        dictonary[team1][loss] +=  1
        dictonary[team2][win] +=  1
    

for each in dictonary:
    dictonary[each]["points"] = dictonary[each]["win"]*3+dictonary[each]["draw"]*1
if num == 0:
    print("No Output")


result_dict = {}
for item in dictonary:
    result_dict["Team: "+item+", Matches Played: "+str(dictonary[item]["win"]
        +dictonary[item]["loss"]+dictonary[item]["draw"])+", Won: "+
        str(dictonary[item]["win"])+", Lost: "+str(dictonary[item]["loss"])+", Draw: "
        +str(dictonary[item]["draw"])+", Points: "+
        str(dictonary[item]["win"]*3+dictonary[item]["draw"]*1)] = dictonary[item]["points"]




r = sorted(result_dict.values(),reverse = True)
for y in r:
    for key,value in result_dict.items():
        if y == value:
            print(key)
    
    
    
    
