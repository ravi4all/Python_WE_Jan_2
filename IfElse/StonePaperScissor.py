import random

cpu_messages = ['stone','paper','scissor']

user_counter = 0
cpu_counter = 0

while True:
    user_input = input("Enter your choice : ")

    cpu_choice = random.choice(cpu_messages)

    if user_input == cpu_choice:
        print("CPU :",cpu_choice)
        print("Match Tie")
    elif user_input == "stone" and cpu_choice == "scissor":
        print("CPU :",cpu_choice)
        print("User win")
        user_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))
    elif user_input == "paper" and cpu_choice == "stone":
        print("CPU :",cpu_choice)
        print("User win")
        user_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))
    elif user_input == "scissor" and cpu_choice == "paper":
        print("CPU :",cpu_choice)
        print("User win")
        user_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))
    elif user_input == "stone" and cpu_choice == "paper":
        print("CPU :",cpu_choice)
        print("CPU win")
        cpu_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))
    elif user_input == "paper" and cpu_choice == "scissor":
        print("CPU :",cpu_choice)
        print("CPU win")
        cpu_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))        
    elif user_input == "scissor" and cpu_choice == "stone":
        print("CPU :",cpu_choice)
        print("CPU win")
        cpu_counter += 1
        print("User : {}    CPU : {}".format(user_counter,cpu_counter))
    else:
        print("Wrong choice...")
    
