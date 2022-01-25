import random


class Faction:
    colors = [
        "Green",
        "Black",
        "Brown",
        "Gray",
        "Blue",
        "Red",
        "Yellow",
        "Ice",
        "Volcano",
        "Variable"
    ]

    @classmethod
    def get_color(cls, player):
        random.shuffle(Faction.colors)
        random.shuffle(Faction.colors)

        draw = Faction.colors.pop()

        accept = input(str(player.get_name()) + " drew " + draw + ". Accept color? (y/n): ")

        if accept.lower() != 'y':
            Faction.colors.append(draw)
            random.shuffle(Faction.colors)
            random.shuffle(Faction.colors)

            draw = Faction.colors.pop()
            print(str(player.get_name()) + " redrew " + draw)

        if draw in ["Ice", "Variable"]:
            temp = []
            expansions = ["Ice", "Volcano", "Variable"]
            for faction in expansions:
                if faction in Faction.colors:
                    Faction.colors.remove(faction)
                    temp.append(faction)

            print("Please choose one of the following as your terrain.")
            Faction.colors.sort()
            print("\t" + ", ".join(Faction.colors))
            choice = input("\tPlease enter your terrain selection: ")
            while choice.capitalize() not in Faction.colors:
                print("\tThat is not a valid terrain option. Please try again.")
                choice = input("\tPlease enter your terrain selection: ")
            else:
                Faction.colors.remove(choice.capitalize())
                draw += " (" + choice.capitalize() + ")"
                Faction.colors.extend(temp)

        player.set_faction(draw)
