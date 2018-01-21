hello_intent = ['hello','hi','hey','hi there','hie']
bye_intent = ['bye','bie','take care','see you','ttyl']

print("Welcome User".center(50))

while True:
    user_msg = input("Enter your message : ")

    hello_rply = "Hello, How are you ?"
    bye_rply = "Bye, See you soon !!!"

    if user_msg.lower() in hello_intent:
        print(hello_rply)
    elif user_msg.lower() in bye_intent:
        print(bye_rply)
    else:
        print("I don't understand")
