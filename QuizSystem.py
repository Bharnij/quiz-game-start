class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def questions_remain(self):
        return self.question_number < len(self.question_list)
       
    def next_question(self):

        current_question = self.question_list[self.question_number]

        self.question_number += 1

        user_answer = input(f" Q. {self.question_number} :- {current_question.text} - (True or False ?) Type here -- > ")
        self.check_answer(user_answer, current_question.answer)
    
    
    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("It is the correct answer! Congrats!")
            self.score += 1
        else:
            print('Thats a wrong answer')

        print(f'The correct answer is :- {correct_answer}')
        print(f'Your current score is :- {self.score} out of {self.question_number}')
        print('\n')

        






    

    
