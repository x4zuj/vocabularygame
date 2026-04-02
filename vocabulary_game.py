
# Welcome to the vocabulary game made by 4zuj.
# In this Game you just have to swap the vocabulary and the answers to your use case!
# Have fun using it :D!

import random

vocabulary = ["Apple", "Pear", "Strawberry", "Rasberry", "Masstourism", "Shopping cart", "Digital footprint", "Carbon dioxide"]
answers = ["apfel", "birne", "erdbeere", "himbeere", "massentourismus", "einkaufswagen", "digitaler fußabdruck", "kohlendioxid"]

print("\nWelcome to the Vocabulary trainer!") 
input("Press ENTER to start learning vocabulary.\n") # Just some decoration

def answer_process(user_result, question_index): # Made a function so it looks cleaner and better, right?
    if user_result.lower() == answers[question_index]:
        answer = "correct!\n"
        return answer
    else:
        answer = "incorrect!\n"
        return answer

while True: # I made a while here so it just goes infinitely.
    question_index = random.randint(0, 7)
    user_answer = input(f"Tell me the german word of the Vocabulary: {vocabulary[question_index]}.\n > ")
    answer_type = answer_process(user_result=user_answer, question_index=question_index)
    print(f"Your answer was {answer_type}")
