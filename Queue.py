#A queue is a data structure that follows the LIFO(Last In First Out) principle.
#Example: add some data to queue. queue(a,b,c,d) -> adding e to queue -> queue(a,b,c,d,e)
#Example: pop some data from queue. queue(a,b,c,d,e) -> popping data from queue -> queue(b,c,d,e) and pop(a)

#Example for queue in line 7-12
"""
queue_number=[1,2,3,4,5]
queue_number.append(6)
queue_number.append(7)
print(queue_number)
print(queue_number.pop(0)) #will pop 1 from queue_number
print(queue_number)
"""

#Simple queue program
import os #used for clear screen at cmd

queue_number=[] #list queue
loop=1 #variable for loop menu
choice=0 #variable for choice menu

#function adding some data
def add_data_queue():
	input_data=int(input("Data input: "))
	queue_number.append(input_data) #add input_data to queue_number
	print("Data is input to list")
	input("Press enter to continue...")

def pop_data_queue():
	if not queue_number: #checking is list empty
		print("List is empty")
	else:
		pop_data=queue_number.pop(0) #pop data from queue_number
		print("Your popped: %d"%pop_data)
	input("Press enter to continue...")

def list_data_queue():
	if not queue_number: #checking is list empty
		print("List is empty")
	else:
		print("Data list: ")
		print(queue_number) #see list data from queue_number

#function menu
def menu_queue():
	print("=-=-= queue Program =-=-=")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
	list_data_queue()
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("1. Add data")
	print("2. Pop data")
	print("3. Exit")


while loop==1: #looping for menu
	os.system('cls') #clear screen on cmd
	menu_queue() #called menu_queue function
	choice=int(input("Your choice: ")) #input for menu decision
	if choice==1: #decision 1
		add_data_queue() #called add_data_queue function
	elif choice==2: #decision 2
		pop_data_queue() #called pop_data_queue function
	elif choice==3: #decision 4
		os.system('cls') #clear screen on cmd
		break #break the loop(end looping).
	else: #another decision condition which didn't in if branch(in this case choice!=1,2,3)
		os.system("cls") #clear screen on cmd