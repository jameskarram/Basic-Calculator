def display_options(): 
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    Func_Choice = input("Choose a number:")
    Func_Choice = int(Func_Choice)
    return Func_Choice

#ASKING USER FOR NUMBERS TO USE IN FUNCTIONS
def ask_user_for_numbers():
  Num1 = input("What is the first number?") 
  Num1 = int(Num1)
  Num2 = input("What is the second number?")
  Num2 = int(Num2)
  return Num1, Num2

def ask_user_for_number(): 
  Num2 = input("What is the second number? ")
  Num2 = int(Num2)
  return Num2

#FUNCTIONS FOR OPERATIONS
def addFunction(x,y):
  result = x + y
  return result

def subFunction(x,y):
  result = x - y
  return result

def divFunction(x,y):
  result = x / y
  return result

def multFunction(x,y):
  result = x * y
  return result

#PUTTING NUMBERS IN RELEVANT FUNCTION
def choose_func(z, a, b): 
  Func_Choice = z
  Num1, Num2 = a, b
  if Func_Choice == 1:
    result = addFunction(Num1, Num2)
    print(result)

  elif Func_Choice == 2:
    result = subFunction(Num1, Num2)
    print(result)

  elif Func_Choice == 3:
    result = divFunction(Num1, Num2)
    print(result)

  elif Func_Choice == 4:
    result = multFunction(Num1, Num2)
    print(result)

  return result

def check_if_user_finished():
  fin_calc = input("Are you finished with your calculations? Yes or No?")
  fin_calc = fin_calc.lower()
  if fin_calc == "yes":
    print("Shutting off")
    print("...")
    print("..")
    print(".")
    print("\n")
    endThisShitOnceAndForAll = False
    use_ans = "no"
  else:
    use_ans = input("Would you like to use your answer? Yes or No?")
    use_ans = use_ans.lower()
    endThisShitOnceAndForAll = True
  return use_ans, endThisShitOnceAndForAll
  
# --------
  
print("Hello World")
print("This is my Calculator")
want_to_use = input("Would you like to use my calculator? Yes or No?")
want_to_use = want_to_use.lower()

if want_to_use == "yes":
  runUserCode = True
else:
  runUserCode = False

use_ans = "no"

while runUserCode:
  Func_Choice = display_options()
  if use_ans == "yes":
    Num1 = result
    Num2 = ask_user_for_number()
  else:
    Num1, Num2 = ask_user_for_numbers()

  result = choose_func(Func_Choice, Num1, Num2) 
  things = check_if_user_finished()
  use_ans = things[0]
  runUserCode = things[1]
