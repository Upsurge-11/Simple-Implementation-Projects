def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-----------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter the option:-")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess :
        print("CORRECT!!")
        return 1
    else:
        print("WRONG!!!")
        return 0

def display_score(correct_guesses,guesses):
    print("-----------------------------------------------------------")
    print("RESULTS!!!")
    print("-----------------------------------------------------------")
    print("Answers: ",end = "")
    for i in questions:
        print(questions.get(i),end = " ")
    print()
    print("Guesses: ",end = "")
    for i in guesses:
        print(i,end = " ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your Score is:- "+str(score)+"%")

def play_again():
    response = input("Do you want to play again? (y/n):")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False

questions = {
    "Who is the best programmer?":"C",
    "Who is your god?":"A",
    "What does your god likes the most?":"B",
    "Who is actually ruling the world?":"D" 
}

options = [["A. Guido Van Rossum","B. Elon Musk","C. Arghyadeep Mukherjee","D. Linus Trovalds"],
          ["A. Arghyadeep Mukherjee","B. Jesus Christ","C. Allah","D. Shiva"],
          ["A. Eating","B. Programming","C. Playing","D. Sleeping"],
          ["A. USA","B. Russia","C. India","D. Arghyadeep"]]

new_game()

while play_again():
    new_game()

print("Have a nice Day !!")