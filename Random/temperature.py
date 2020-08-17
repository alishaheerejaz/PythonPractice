user_input = ''
started= False
while (True):
    user_input = input('> ').lower()
    if user_input == 'start' and not started :
        print("Car started .. Ready to go")
        started = True

    elif user_input == 'start' and started:
        print("Car is already started")

    elif user_input == 'stop' and started:
        print("Car stopped.")
        started = False
    elif user_input == 'stop' and not started:
        print ("Car is already stopped")
    elif user_input == 'help':
        print("""
start - t0 start 
stop = to stop
quit - to quit
        """)
    elif user_input == "quit":
        break
    else:
        print("I don't understart")
else:
    print("End of session")