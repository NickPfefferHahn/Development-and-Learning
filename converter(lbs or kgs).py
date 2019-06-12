weight = int(input("Please input your weight: "))

converter = input("(L)bs or (K)g: ")

if converter.upper() == "L":
    print(f"you weigh {float(weight) * .45} kgs!")

elif converter.upper() == "K":
    print(f"you weigh {float(weight) / .45} lbs!")

else:
    print("I'm sorry, that is not a valid response.")
