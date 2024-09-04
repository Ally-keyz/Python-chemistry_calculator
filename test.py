import pyttsx3

engine = pyttsx3.init()


operators ={
    "add":"+",
    "subtract":"-",
    "divide":"/",
    "multiply":"*"
}


def main():

    num1 = get_num1()
    num2 = get_num2()
    operator = get_operator()
    operation = perform_operation(num1,num2,operator)

    engine.say(f"The answer is: {operation}")
    engine.runAndWait()
    print(f"The answer is: {operation}")


def get_num1():
    while True:
        try:
            num = int(input("Enter a number: "))

        except ValueError:
            engine.say("Please enter a number")
            engine.runAndWait()

        return num


def get_num2():
    while True:
        try:
            num = int(input("Enter a number: "))

        except ValueError:
            engine.say("Please enter a number")
            engine.runAndWait()
            return None

        return num        


def get_operator():
    operat = input("select an operation(add,subtract,divide,multiply): ").lower()

    if operat in operators:
        return operators[operat]

    else:
        engine.say("The operator is not in the selection list")
        engine.runAndWait()
        return None    



def perform_operation(num1,num2,operator):
    try:
        result = eval(f"{num1} {operator} {num2}")
        return result

    except Exception as e:
        engine.say("There was error please try again")
        engine.runAndWait()
        print(f"the error is {e}")
        return None



main()

               



