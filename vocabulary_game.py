
# Welcome to the vocabulary game made by 4zuj.
# In this Game you just have to swap the vocabulary and the answers to your use case!
# Have fun using it :D!

import random

vocabulary = ["Apple", "Pear", "Strawberry", "Rasberry", "Masstourism", "Shopping cart", "Digital footprint", "Carbon dioxide"]
answers = ["apfel", "birne", "erdbeere", "himbeere", "massentourismus", "einkaufswagen", "digitaler fußabdruck", "kohlendioxid"]

print("\nWelcome to the Vocabulary trainer!") 
input("Press ENTER to start learning vocabulary.\n") # Just some decoration

def answer_process(sample_result, user_result): # Made a function so it looks cleaner and better, right?
    answer_text = "Your answer was"
    if user_result.lower() in sample_result:
        answer = print("correct!\n")
        return answer
    else:
        answer = print("incorrect!\n")
        return answer

while True: # I made a while here so it just goes infinitely.
    question = random.choice(vocabulary)
    user_answer = input(f"Tell me the german word of the Vocabulary: {question}.\n > ")
    answer_process(sample_result=answers, user_result=user_answer)
