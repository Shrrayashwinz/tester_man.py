my_list = ["Leonardo", "Raphael", "Donatello", "Jaylenando", "Michelangelo"]

def print_list():
    ninja_turtle = True
    while ninja_turtle:
        print(my_list)
        ninja_turtle = input("Do you want to add the turtles again [yes / no]?").upper()
        if ninja_turtle == "no":
            ninja_turtle = False

    else:
        print("I hope u liked dis program!")

if __name__ == "__main__":
    print_list()


