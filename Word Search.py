import random
listofletters = []
for i in range(120):
    x = random.randint(1, 26)
    letterlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    x = x-1
    letters = letterlist[x]
    listofletters.append(letters)
print("WORDSEARCH")
gameon = True
while gameon == True:
    howhard = input("would you like easy, medium, hard, or leave? ")
    if howhard == "easy":
        difficulty = "easy"
        length = 7
    elif howhard == "medium":
        difficulty = "medium"
        length = 9
    elif howhard == "hard":
        difficulty = "hard"
        length = 15
    elif howhard == "leave":
        gameon =False
        quit(code="thanks for playing")
    r = open("listofwords.txt", "r")
    listofwords=[]
    t = r.readline()
    listofwords.append(t)
    print(listofwords)
    finalwordlist = []
    for e in range(length):
        randomI = random.randint(0, 998)
        finalwordlist.append(listofwords[randomI])

    print(finalwordlist)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    grid = []


    if difficulty == "easy":
        numofwords = 5
    if difficulty == "medium":
        numofwords = 10
    if difficulty == "hard":
        numofwords = 15

    for i in range(length):
        grid.append([])
        for j in range(length):
            letter = random.randint(0, 25)
            grid[i].append(alphabet[letter])
        print(grid[i])