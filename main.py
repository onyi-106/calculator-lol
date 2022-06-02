def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

saved_answer = 0

num1 = int(input("What's the first number? "))
for i in operations:
  print(i)
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the second number? "))

calculation = operations[operation_symbol]
answer = calculation(n1=num1, n2=num2)
saved_answer += answer


print(f"{num1} {operation_symbol} {num2} = {answer}")


# direction = input(f"Type 'y' to continue calculating with {answer}, type 'n' to stop.")
# if direction == "n":
  # print("End of command.")
# else:
  # num3 = int(input("What's the next number? "))

def fullver_calc(saved_answer):
  def direction():
    direction = input(f"Type 'y' to continue calculating with {answer}, type 'n' to stop.")
    if direction == "n":
      print(f"Calculator ended with the result: {saved_answer}")
      return True
  
  end_of_command = direction()
  
  while not end_of_command:
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(n1=saved_answer, n2=num3)
    print(f"{saved_answer} {operation_symbol} {num3} = {second_answer}")
    saved_answer = second_answer
    
    end_of_command = direction()  

fullver_calc(saved_answer)






























# #WHILE LOOP STARTS FROM HERE
# def continous_calc():
#   end_of_command = False
#   while not end_of_command:
#     direction = input(f"Type 'y' to continue calculating with {saved_answer}, type 'n' to stop.")
#     if direction == "n":
#       end_of_command = True
#       return
      
  
#     operation_symbol = input("Pick an operation: ")
#     next_num = int(input("What's the next number? "))
#     # saved_answer calculate next_num
  
#     saved_answer += calculation(n1=saved_answer, n2=next_num)
#     print(saved_answer)

# continous_calc()