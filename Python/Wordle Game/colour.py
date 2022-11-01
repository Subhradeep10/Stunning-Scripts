
__all__ = [
    "B", "BB", "BU",
    "G", "GB", "GU",
    "R", "RB", "RU",
    "Y", "YB", "YU"
]

class Colour:
    colour_code = {
        "blue" : 96,
        "green" : 92,
        "red" : 91,
        "yellow" : 93
    }

    @staticmethod
    def colour(colour, msg):
        return f"\33[0;49;{colour}m{msg}\33[0m"

    @staticmethod
    def colour_block(colour, msg):
        return f"\33[7;49;{colour}m{msg}\33[0m"

    @staticmethod
    def colour_underline(colour, msg):
        return f"\33[4;49;{colour}m{msg}\33[0m"

    blue = lambda msg : Colour.colour(Colour.colour_code["blue"], msg)
    blue_block = lambda msg : Colour.colour_block(Colour.colour_code["blue"], msg)
    blue_underline = lambda msg : Colour.colour_underline(Colour.colour_code["blue"], msg)

    green = lambda msg : Colour.colour(Colour.colour_code["green"], msg)
    green_block = lambda msg : Colour.colour_block(Colour.colour_code["green"], msg)
    green_underline = lambda msg : Colour.colour_underline(Colour.colour_code["green"], msg)

    red = lambda msg : Colour.colour(Colour.colour_code["red"], msg)
    red_block = lambda msg : Colour.colour_block(Colour.colour_code["red"], msg)
    red_underline = lambda msg : Colour.colour_underline(Colour.colour_code["red"], msg)

    yellow = lambda msg : Colour.colour(Colour.colour_code["yellow"], msg)
    yellow_block = lambda msg : Colour.colour_block(Colour.colour_code["yellow"], msg)
    yellow_underline = lambda msg : Colour.colour_underline(Colour.colour_code["yellow"], msg)



B = Colour.blue
BB = Colour.blue_block
BU = Colour.blue_underline

G = Colour.green
GB = Colour.green_block
GU = Colour.green_underline

R = Colour.red
RB = Colour.red_block
RU = Colour.red_underline

Y = Colour.yellow
YB = Colour.yellow_block
YU = Colour.yellow_underline
