valid_answer = [
    '42',
    'forty-two',
    'forty two'
]

question = "What is the Answer to the Great Question of Life, the Universe, and Everything? "

user_answer = input(question).lower().strip()

# print(user_answer)

if user_answer in valid_answer:
    print("Yes")
else:
    print("No")
