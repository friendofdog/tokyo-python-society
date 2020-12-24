import pyinputplus as pyip

def verify_input_manually():
    while True:
        age = input("Enter your age: ")
        try:
            age = int(age)
        except:
            print("Please use numeric digits.")
            continue
        if age < 1:
            print("Please enter a positive number.")
            continue
        break

    print(f"Your age is {age}.")

def verify_input_pyip():
    age = pyip.inputNum("Enter your age: ", min=1)
    print(f"Your age is {age}.")

def no_final_vowel():
    string = pyip.inputStr("Enter your phone number: ",
                           blockRegexes=[r"[aeiou]$"])
    print(f"This string does not end with a vowel: {string}")
