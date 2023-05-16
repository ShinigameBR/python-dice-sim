import random


def rollDice():
    roll = input("Deseja girar os dados? (S/N):")

    while roll.lower() == "S".lower():
        dice_one_value = random.randint(1, 6)
        dice_two_value = random.randint(1, 6)
        print(
            f"Os dados rolados resultam em {dice_one_value} e {dice_two_value} respectivamente.")
        print("\n".join(roll_draws[dice_one_value]))
        print("\n".join(roll_draws[dice_two_value]))

        roll = input("Deseja girar os dados novamente? (S/N):")


roll_draws = {
    1: (
        "-----------",
        "|         |",
        "|    o    |",
        "|         |",
        "-----------",
    ),
    2: (
        "-----------",
        "|o        |",
        "|         |",
        "|        o|",
        "-----------",
    ),
    3: (
        "-----------",
        "|o        |",
        "|    o    |",
        "|        o|",
        "-----------",
    ),
    4: (
        "-----------",
        "|o       o|",
        "|         |",
        "|o       o|",
        "-----------",
    ),
    5: (
        "-----------",
        "|o       o|",
        "|    o    |",
        "|o       o|",
        "-----------",
    ),
    6: (
        "-----------",
        "|o       o|",
        "|o       o|",
        "|o       o|",
        "-----------",
    )
}

rollDice()
