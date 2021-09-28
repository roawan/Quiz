def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes/y or no/n")
show_instructions = yes_no("Would you like to view instructions?")

instructions = "Every Round you will be asked a question about the Call of Duty: Modern Warfare installments.\nThese will be based on the plot, characters and weaponry of the series.\n To advance the round press enter and to answer simply type desire answer when prompted"


if show_instructions == "yes" or show_instructions == "y":
    print(instructions)


instructions = "Every Round you will be asked a question about the Call of Duty: Modern Warfare series.\nThese will be based on the plot, characters and weaponry of the series.\nTo advance the round press enter and to answer simply type your desired answer when prompted"

