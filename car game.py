start = "The car is started"
stop = "You have stopped the car"
help_me = """
start - to start the car
stop - to stop the car
quit - to exit game"""
phase_one = input("> ")
while phase_one.lower() == "start":
    print(start)
    break
phase_one = input("> ")
while phase_one.lower() == "stop":
    print(stop)
    break
phase_one = input("> ")
while phase_one.lower() == "help":
    print(help_me)
    break
phase_one = input("> ")
while phase_one.lower() == "quit":
    break
print("Program ended")
