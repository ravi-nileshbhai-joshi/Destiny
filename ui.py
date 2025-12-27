def get_name():
    name = input("Enter you name: ")
    return name

def get_state(name):
    energy = int(input(name + " Rate your energy (1-10): "))
    focus = int(input(name + " Rate your focus (1-10): "))
    return energy, focus 

def display_result(name, recommendation):
    print(f"{name}, your recommendation: {recommendation}")
    