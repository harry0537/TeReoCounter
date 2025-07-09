import csv
import random

# Two Lists to import individual columns in the text file.
englishwords = []
maoriwords = []
# imported file as csv
try:
    with open("Maori2Eng.txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)  # read the comma separated values.
        for line in csv_reader:
            englishwords.append(line[1])  # separate english words from file in list.
            maoriwords.append(line[0])  # separate maori words from file in list.
except FileNotFoundError:
    print("Error: Maori2Eng.txt file not found. Please make sure it is in the same directory as the script.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading Maori2Eng.txt: {e}")
    exit(1)

def get_valid_input(prompt, valid_options=None, allow_exit=True):
    """Get valid user input with option to exit."""
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if allow_exit and user_input in ['exit', 'quit', 'q']:
                print("\nExiting program. Goodbye!")
                exit(0)
            if valid_options is None:
                return user_input
            if user_input in valid_options:
                return user_input
            else:
                print(f"Please enter a valid option: {', '.join(valid_options)}")
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Exiting program.")
            exit(0)

# quiz1
def inputmode():
    print("\n" + "="*50)
    print("           INPUT MODE QUIZ")
    print("="*50)
    print("You will be given 10 English words.")
    print("Type the Maori translation for each word.")
    print("Type 'exit' at any time to quit the quiz.\n")
    
    ewords = englishwords.copy()  # makes a copy of the lists from above, as we will be removing items to prevent duplicates.
    mwords = maoriwords.copy()  # same as above.
    score = 0  # score counter.
    border = "✦•······················•✦•······················•✦"
    border2 = "════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════════ ⋆X⋆ ════"
    try:
        rando1 = random.sample(range(len(ewords)), 10)  # 10 random numbers generated from the length of the list.
    except ValueError:
        print("Not enough words in the list to generate 10 questions.")
        return
    x_list = []  # list to append used questions to avoid duplicates.
    for i in rando1:  # up to the value of rando1(10).
        e1 = ewords[i]  # picks english word.
        m1 = mwords[i]  # picks its maori translation from the same index for comparison.
        print("       Your english word is", e1.upper())
        answer = get_valid_input("       Please provide Maori translation: ")
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
    return

# quiz 2
def multichoicemode():
    print("\n" + "="*50)
    print("        MULTI-CHOICE MODE QUIZ")
    print("="*50)
    print("You will be given 10 English words.")
    print("Select the correct Maori translation from 4 options.")
    print("Type 'exit' at any time to quit the quiz.\n")
    
    global eword, mindex, mm1, eindex
    ewords = englishwords.copy()  # same as inputmode
    mwords = maoriwords.copy()  #same as inputmode
    score = 0  #sameasinputmode
    counter = 0
    border = "✦•······················•✦•······················•✦"
    border2 = "●○●○●○●○●○● ●○●○●○●○●○●●○●○●○●○●○● ●○●○●○●○●○●"

    while counter < 10:
        try:
            rando2 = random.sample(range(len(ewords)), 4)  # generating the options
        except ValueError:
            print("Not enough words in the list to generate options.")
            return
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

        print(f"Question {counter + 1}/10:")
        statement1 = "Select the Maori translation for " + eword.upper() + ": \n"
        for (m1, mlist_item) in enumerate(mlist, start=1):
            print(f"{m1}. {mlist_item}")
        ans = get_valid_input(statement1, ['1', '2', '3', '4'])
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

    print(border2)
    print("            You scored %d out of 10" % score)
    print(border2)
    print("\n\n\n")
    return

# quizselection
def quizselect():
    while True:
        print("\n" + "="*50)
        print("           TEREOCUNTER QUIZ")
        print("="*50)
        print("Welcome to the Maori language learning quiz!")
        print("Choose your quiz mode:")
        print("1. Input Mode - Type the Maori translation")
        print("2. Multi-Choice Mode - Select from options")
        print("3. Exit")
        print("="*50)
        
        choice = get_valid_input("Please select your mode (1, 2, or 3): ", ['1', '2', '3'])
        
        if choice == "1": 
            inputmode()
        elif choice == "2": 
            multichoicemode()
        elif choice == "3":
            print("\nThank you for using TeReoCounter! Goodbye!")
            exit(0)
        
        # Ask if user wants to play again
        play_again = get_valid_input("\nWould you like to play again? (y/n): ", ['y', 'n', 'yes', 'no'])
        if play_again in ['n', 'no']:
            print("\nThank you for using TeReoCounter! Goodbye!")
            exit(0)

if __name__ == "__main__":
    quizselect()