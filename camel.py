camel_case = input("camelCase: ")
snake_case = ""
for letter in camel_case:
    if letter.islower():
        snake_case +=letter
    else:
        snake_case +="_"+letter.lower()
print("snake_case: "+snake_case)
