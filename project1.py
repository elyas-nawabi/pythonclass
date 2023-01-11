from string import ascii_lowercase
import emoji
# questions = [
#     ("when was invented internet", "1970"),
#     ("who invented python, ", "vanrossum")
# ]
# enumerate()  -> count, value

questions = {
    "which one is a loop in python?" : ["for", "none", "if", "switch"],
    "which one is a correct variale in python" : ["name", "name123", "if", "break"],
    "with which language we build dynamic websites?" : ["python", "css", "html", "none"],
    "which one is a keyword in python" : ["def", "iff", "elsee", "function"],
}
# letters = ['','a','b','c','d']
for num , (question, alternatives) in enumerate(questions.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}")
    correct_answer = alternatives[0]
    labeled_choices = dict(zip(ascii_lowercase, sorted(alternatives)))

    for label, choice in labeled_choices.items():
        print(f" {label}) {choice}")

    answer_label = input(f"\nChoice? ")
    answer = labeled_choices.get(answer_label)
    if answer == correct_answer:
        print(" \n{winking face}  correct!")
    else: 
        print(f"The answer is {correct_answer}, not {answer}")





# for question, alternatives in questions.items():
#     correct_answer = alternatives[0]
#     sorted_choices = sorted(alternatives)
#     for label, choice in enumerate(sorted_choices):
#         print(f" {label}) {choice}")

#     answer_label = int(input(f"{question} "))
#     answer = sorted_choices[answer_label]
#     if answer == correct_answer:
#         print(" correct!")
#     else: 
#         print(f"The answer is {correct_answer}, not {answer}")
        
        
    








# for question, correct_answer in questions:
#     answer = input(f"{question}")
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer}, not {answer}")
        
    
    