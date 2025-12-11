# Quiz Game

class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_list = [
    "\nWhat is the full form of OOP?\n"
    " a. Object Oriented Programming\n"
    " b. Object Obtained Program\n"
    " c. Orientation Objection Programming\n"
    " d. Option Object Paragraph\n",

    "\nWhat is a dictionary in Python?\n"
    " a. str\n"
    " b. list\n"
    " c. dict\n"
    " d. tuble\n",

    "\nWhich keyword is used to create a function in Python?\n"
    " a. define\n"
    " b. def\n"
    " c. func\n"
    " d. function\n",

    "\nWhich data type is immutable in Python?\n"
    " a. List\n"
    " b. Dictionary\n"
    " c. Tuple\n"
    " d. Set\n",

    "\nWhich operator is used for exponentiation in Python?\n"
    " a. ^\n"
    " b. ^^\n"
    " c. exp\n"
    " d. **\n"
]


quiz_list = [
    Quiz(question_list[0], "a"),
    Quiz(question_list[1], "c"),
    Quiz(question_list[2], "b"),
    Quiz(question_list[3], "c"),
    Quiz(question_list[4], "d")
]


def show(quiz_list):
    score = 0
    for i in quiz_list:
        user = input(i.question + "Your answer: ").lower()

        if user == i.answer:
            score += 1

    print(f"\nTotal score: {score}/{len(quiz_list)}")


show(quiz_list)
