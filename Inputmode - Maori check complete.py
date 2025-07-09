import csv
import random

# Two Lists to import individual columns in the text file.
englishwords = []
maoriwords = []
# imported file as csv
with open("E:\Harry\Programming Fundamentals\Maori2Eng.txt", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # read the comma separated values.
    for line in csv_reader:
        englishwords.append(line[1])  # separate english words from file in list.
        maoriwords.append(line[0])  # separate maori words from file in list.

# quiz1
def inputmode():
    ewords = englishwords  # makes a copy of the lists from above, as we will be removing items to prevent duplicates.
    mwords = maoriwords  # same as above.
    score = 0  # score counter.
    rando1 = []  # list to append 10 random questions.
    border = "✦•······················•✦•······················•✦"
    border2 = "════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════"
    rando1 = random.sample(range(len(ewords)), 10)  # 10 random numbers generated from the length of the list.
    x_list = []  # list to append used questions to avoid duplicates.
    for i in rando1:  # up to the value of rando1(10).
        e1 = ewords[i]  # picks english word.
        m1 = mwords[i]  # picks its maori translation from the same index for comparison.
        print("       Your english word is", e1.upper())
        answer = input("       Please provide Maori translation: ")  # Answer prompt
        if answer.upper() == m1.upper():  # Answer comparison by converting both to upper case.
            print("\n",border)
            print("          Congratulations, You are correct!")
            print("              ", answer.upper(), "is the right answer!")
            print(border)
            print("\n\n                   NEXT QUESTION \n")
            score = score + 1  # score is updated if answer is correct
            x_list.append(ewords.pop(ewords.index(e1)))  # removes the used word from the ewords list & appends it to the x_list.
        else:
            print("\n",border2)
            print("                Sorry, You are wrong!")
            print("               Correct answer is " + m1.upper())
            print(border2)
            print("\n                   NEXT QUESTION \n")
    print("●○●○●○●○●○● ●○●○●○●○●○●●○●○●○●○●○● ●○●○●○●○●○●")
    print("            You scored %d out of 10" % score)  # score is displayed in the end.
    print("●○●○●○●○●○● ●○●○●○●○●○●●○●○●○●○●○● ●○●○●○●○●○●\n\n\n")
    quizselect()
    return
# quiz 2
def multichoicemode():
    global eword, mindex, mm1, eindex
    ewords = englishwords  # same as inputmode
    mwords = maoriwords  #same as inputmode
    score = 0  #sameasinputmode
    counter = 0
    border = "✦•······················•✦•······················•✦"
    border2 = "●○●○●○●○●○● ●○●○●○●○●○●●○●○●○●○●○● ●○●○●○●○●○●"

    while counter < 11:
        rando2 = []  # list of 4 options(1 correct, 3 wrong)
        rando2 = random.sample(range(len(ewords)), 4)  # generating the options
        elist = []
        mlist = []
        x_list = []

        for i in rando2:
            e1 = ewords[i].upper()
            m1 = mwords[i].upper()
            elist.append(e1)
            mlist.append(m1)
            eword = random.choice(elist)
            eindex = elist.index(eword)
            mindex = eindex + 1
            mm1 = mlist[eindex].upper()


        statement1 = "Select the maori translation for " + eword.upper() + ": \n"
        for (m1, mlist) in enumerate(mlist, start=1):
            print(m1, mlist)
        ans = input(statement1)

        if ans == str(mindex):
            print("\n"+border)
            print("          Congratulations, You are correct!")
            print("            ", mm1, "is the right answer!")
            print(border)
            print("\n NEXT QUESTION \nYour Options:")
            score = score + 1
            x_list.append(ewords.pop(eindex))
            counter = counter + 1
        elif ans != str(mindex):
            print("\n════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════\n               Sorry, you are Wrong! \n              Right answer is %s\n════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════\n" % mm1)
            x_list.append(ewords.pop(eindex))
            print("\nNEXT QUESTION \nYour Options:")
            counter = counter + 1
        else:
            print("Please select a valid option!")

    print(border2)
    print("            You scored %d out of 10" % score)
    print(border2)
    print("\n\n\n")
    quizselect()
    return


# quizselection
def quizselect():
    print("1. Input Mode \n2. Multi-Choice Mode")
    a = input("Please select your mode: ")
    if a == "1": inputmode()
    elif a == "2": multichoicemode()
    else:
        print("Please select a valid option!")
    return


quizselect()