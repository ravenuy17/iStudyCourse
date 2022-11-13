def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again: ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
#Question 1
print("We already learned enough to answer our first quiz question")
print("Which computer language structures all web pages on the internet?")
question1 = input("a)CSS\nb)JavaScript\nc)HTML\nd)Python\n:")
check_guess(question1,"c")

#Question 2
print("In HTML, things revolve around tags. Tags start with <, followed by a keyword, then finished with a >")
question2= input("a)<p>\nb){p}\nc)(p)\nd)[p]\n:")
check_guess(question2,"a")

#Question 3
print("What do you think comes after the opening tag?")
question3= input("a)Opening tag: <p>\nb)Closing tag: </p>\n:")
check_guess(question3,"b")

#Question 4
print("What do you think comes after the opening tag?\n <p> Hello World! </p>")
question3= input("a)A video\nb)A text that will display “Hi!”\nc)A paragraph that will display a “Hello World”\nd)An image\n:")
check_guess(question3,"c")

#Question 5
print("What is the missing symbol in a closing tag?\n <p> Hi <__p>")
question5= input("a)<\nb)/\nc)>\nd)\\n:")
check_guess(question5,"b")

print("Your Score is "+ str(score))