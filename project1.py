# questions = [
#     ("when was invented internet", "1970"),
#     ("who invented python, ", "vanrossum")
# ]
questions = {
    "which one is a loop in python?" : ["for", "none", "if", "switch"],
    "which one is a correct variale in python" : ["name", "name123", "if", "break"],
    "with which language we build dynamic websites?" : ["python", "css", "html", "none"],
    "which one is a keyword in python" : ["def", "iff", "elsee", "function"],
}

for question, alternatives in questions.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f" {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print(" correct!")
    else: 
        print(f"The answer is {correct_answer}, not {answer}")
        
        
    








# for question, correct_answer in questions:
#     answer = input(f"{question}")
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer}, not {answer}")
        
    
    