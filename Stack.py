#A Stack is a data structure that follows the LIFO(Last In First Out) principle.
#Example: add some data to stack. stack(a,b,c,d) -> adding e to stack -> stack(a,b,c,d,e)
#Example: pop some data from stack. stack(a,b,c,d,e) -> popping data from stack -> stack(a,b,c,d) and pop(e)

#Example for stack in line 7-12
"""
Stack_number=[1,2,3,4,5]
Stack_number.append(6)
Stack_number.append(7)
print(Stack_number)
print(Stack_number.pop()) #will pop 7 from Stack_number
print(Stack_number)
"""

#Simple Stack program
import os #used for clear screen at cmd

Stack_number=[] #list Stack
loop=1 #variable for loop menu
choice=0 #variable for choice menu

#function adding some data
def add_data_Stack():
	input_data=int(input("Data input: "))
	Stack_number.append(input_data) #add input_data to Stack_number
	print("Data is input to list")
	input("Press enter to continue...")

def pop_data_Stack():
	if not Stack_number: #checking is list empty
		print("List is empty")
	else:
		pop_data=Stack_number.pop() #pop data from Stack_number
		print("Your popped: %d"%pop_data)
	input("Press enter to continue...")

def list_data_Stack():
	if not Stack_number: #checking is list empty
		print("List is empty")
	else:
		print("Data List: ")
		print(Stack_number) #see list data from Stack_number

#function menu
def menu_Stack():
	print("=-=-= Stack Program =-=-=")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
	list_data_Stack()
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("1. Add data")
	print("2. Pop data")
	print("3. Exit")


while loop==1: #looping for menu
	os.system('cls') #clear screen on cmd
	menu_Stack() #called menu_Stack function
	choice=int(input("Your choice: ")) #input for menu decision
	if choice==1: #decision 1
		add_data_Stack() #called add_data_Stack function
	elif choice==2: #decision 2
		pop_data_Stack() #called pop_data_Stack function
	elif choice==3: #decision 4
		os.system('cls') #clear screen on cmd
		break #break the loop(end looping).
	else: #another decision condition which didn't in if branch(in this case choice!=1,2,3)
		os.system("cls") #clear screen on cmd