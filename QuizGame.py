print('*********************************************')
print('\n Welcome to My Quiz Game!!!!!!!!!!!!!!!!!!! \n')
print('*********************************************')

Question_bank = [
    {'que':'What is the primary goal of Object Oriented Programming','ans':'a'},
    {'que':'In python, What is a Class','ans':'d'},
    {'que':'What is an instance variable in a class','ans':'c'},
    {'que':'What is encapsulation in a Objct Oriented Programming','ans':'c'},
    {'que':'What is Polymorphism in OOP','ans':'c'}
]

Options = [
    ['A. Code reusability and modularity','B. Effecient memory utilization','C. Procedural abstraction','D. Dynamic typing'],
    ['A. Function', 'B. module', 'C. Code Block', 'D. Blueprint'],
    ['A. A variable shared among all instance of class', 'B. A variable shared among different class','C. A variable specific to an instance', 'D. A variable used for method overloading'],
    ['A. A process of converting class into a module', 'B. Combining multiple class into one', 'C. Restricting access to certain components of an object and hiding implementation details', 'D. Creating a new instance of a class'],
    ['A. Combining multiple class into one', 'B. Restricting access to main components of an object', 'C. Defining multiple methods in same name in a class', 'D. Providing a single interface with different types']
]

score = 0
def check_answer(a,b):
    if a == b:
        return True
    else:
        return False


for question_num in range(len(Question_bank)):
    print('\n************************************************\n')
    print(Question_bank[question_num]['que'])
    for i in Options[question_num]:
        print(i) 
    

    guess = input('Enter the correct answer (A/B/C/D) : ')

    if check_answer(guess, Question_bank[question_num]['ans']):
        print(' Correct Answer ')
        score += 1
    else:
        print(' Incorrect Answer ')
        print(f'The correct answer is {Question_bank[question_num]['ans']}')

print (f'Your total Correct Answers are {score} out of {len(Question_bank)}')
scored_percentage = (score/len(Question_bank))*100
print ('Percentage :', scored_percentage)