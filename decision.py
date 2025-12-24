energy = int(input("Rate your energy (1-10:) "))
focus = int(input("Rate your focus (1-10): "))

if energy >=7 and focus >=7:
    print("Deep work")
elif energy >=7 and focus <7:
    print("Physical task or learning")
elif energy >=4 and focus >=4:
    print("Light work")
elif energy <4:
    print("Rest")
else:
    print("Relax and reset")
    