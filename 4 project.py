import sys

############################################################

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except IOError as e:
        print("Sorry, invalid response")
        input("Press enter to exit")
        sys.exit()
    else:
        return file

############################################################
def read_line(file):
    line = file.readline()
    line = line.replace("/", "\n")
    return line

############################################################
def next_block(file):
    category = read_line(file)
    question = read_line(file)
    answers = []
    for i in range(4):
        answer = read_line(file)
        answers.append(answer)
    correct = read_line(file)
    if correct:
        correct = correct[0]
    explanation = read_line(file)
    return category, question, answers, correct, explanation

############################################################
def welcome(title):
    """Welcom the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

############################################################
def main():
    file = open_file("test_file.txt", "r")
    title = read_line(file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1, answers[i])
        answer = input("Put in what you think is the answer: ")
        if answer == correct:
            print("You got it, nice")
            score += 1
        else:
            print("Nope, that's incorrect")
        print(explanation)
        print(score)
        category, question, answers, correct, explanation = next_block(file)
    file.close()
    print("You've completed the quiz")
    return score

############################################################    
show = main()
print(show)

############################################################

    
    





















