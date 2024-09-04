
import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

operators ={
    "add": "+",
    "subtract":"-",
    "divide":"/",
    "multiply":"*"
}

def main():

    num1 = get_num1()
    num2 = get_num2()
    operator = get_operator()

    operation = perform_operation(num1 , num2 , operator)

    engine.say(f"the answer is: {operation}")
    engine.runAndWait()
    print(f"the answer is: {operation}")


def get_num1():
    while True:
        try:
            numA = int(input("Enter first number: "))
        
        except ValueError:
            print("please enter a number!!")
           
        return numA

   




def get_num2():

    while True:
        try:
            numB= int(input("Enter first number: "))
        except ValueError:
            engine.say("please enter a number")
            engine.runAndWait()
        return numB 



def get_operator():

    operand = input("Enter operation (add, subtract, divide, multiply): ").lower()
    if operand in operators:
        return operators[operand]
        
    else:
        print("Invalid operator! Please try again.")
        engine.say("Invalid operator! Please try again.")
        engine.runAndWait() 
           
          
    



def perform_operation(num1,num2,operator):

    try:
        result = eval(f"{num1} {operator} {num2}")
        return result

    except Exception as e:
        engine.say("There was an error. Please try again.")
        engine.runAndWait()
        print(f"Error: {e}")
        return None    
        
main()
