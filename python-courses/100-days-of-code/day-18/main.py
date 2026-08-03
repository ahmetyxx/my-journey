from turtle import Turtle, Screen
import random as r
import colorgram
import math

colors_list = [
    {"name": "alice blue", "hex": "#f0f8ff", "rgb": (240, 248, 255)},
    {"name": "black", "hex": "#000000", "rgb": (0, 0, 0)},
    {"name": "blue", "hex": "#0000ff", "rgb": (0, 0, 255)},
    {"name": "brown", "hex": "#a52a2a", "rgb": (165, 42, 42)},
    {"name": "chocolate", "hex": "#d2691e", "rgb": (210, 105, 30)},
    {"name": "coral", "hex": "#ff7f50", "rgb": (255, 127, 80)},
    {"name": "crimson", "hex": "#dc143c", "rgb": (220, 20, 60)},
    {"name": "cyan", "hex": "#00ffff", "rgb": (0, 255, 255)},
    {"name": "dark blue", "hex": "#00008b", "rgb": (0, 0, 139)},
    {"name": "dark green", "hex": "#006400", "rgb": (0, 100, 0)},
    {"name": "dark orange", "hex": "#ff8c00", "rgb": (255, 140, 0)},
    {"name": "dark red", "hex": "#8b0000", "rgb": (139, 0, 0)},
    {"name": "deeppink", "hex": "#ff1493", "rgb": (255, 20, 147)},
    {"name": "dodger blue", "hex": "#1e90ff", "rgb": (30, 144, 255)},
    {"name": "forest green", "hex": "#228b22", "rgb": (34, 139, 34)},
    {"name": "gold", "hex": "#ffd700", "rgb": (255, 215, 0)},
    {"name": "gray", "hex": "#808080", "rgb": (128, 128, 128)},
    {"name": "green", "hex": "#008000", "rgb": (0, 128, 0)},
    {"name": "hot pink", "hex": "#ff69b4", "rgb": (255, 105, 180)},
    {"name": "indigo", "hex": "#4b0082", "rgb": (75, 0, 130)},
    {"name": "ivory", "hex": "#fffff0", "rgb": (255, 255, 240)},
    {"name": "khaki", "hex": "#f0e68c", "rgb": (240, 230, 140)},
    {"name": "lavender", "hex": "#e6e6fa", "rgb": (230, 230, 250)},
    {"name": "lime", "hex": "#00ff00", "rgb": (0, 255, 0)},
    {"name": "magenta", "hex": "#ff00ff", "rgb": (255, 0, 255)},
    {"name": "maroon", "hex": "#800000", "rgb": (128, 0, 0)},
    {"name": "navy", "hex": "#000080", "rgb": (0, 0, 128)},
    {"name": "olive", "hex": "#808000", "rgb": (128, 128, 0)},
    {"name": "orange", "hex": "#ffa500", "rgb": (255, 165, 0)},
    {"name": "white", "hex": "#ffffff", "rgb": (255, 255, 255)},
]


jhan = Turtle()
my_screen = Screen()

my_screen.colormode(255)
jhan.color("red")
jhan.shape("turtle")


def draw_rectangle():
    for i in range(4):
        for _ in range(10):
            jhan.pd()
            jhan.forward(5)
            jhan.pu()
            jhan.forward(5)
        jhan.right(90)


def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return (red, green, blue)


# for i in range(3, 11):
#     angle = 360 / i
#     jhan.pencolor(r.choice(colors_list)["name"])
#     for t in range(i):

#         jhan.forward(100)
#         jhan.right(angle)

# while True:
#     jhan.setpos(r.randint(1,400),r.randint(1,400))


# directions = [0, 90, 180, 270]

jhan.pensize(1)
jhan.speed(3)

# for step in range(200):

#     _color = random_color()  #r.choice(colors_list)["name"]
#     random_direction = r.choice(directions)

#     jhan.color(_color)
#     jhan.forward(30)
#     jhan.setheading(random_direction)


def draw_spirograph(density):
    # spirograph_density=round(360/density)

    for i in range(density):
        jhan.circle(90)
        jhan.color(random_color())
        jhan.left(360 / density)


image_colors = colorgram.extract("image.jpg", 46)


def draw_hirst(row, column):
    gap_row = my_screen.window_width() / row
    gap_column = my_screen.window_height() / column
    for i in range(row * column):  # 36
        pozitionx = -(row / 2) * gap_row + (i % row) * (gap_row)
        pozitiony = (-(column / 2) * gap_column) + (math.ceil(i // row)) * gap_column
        jhan.teleport(pozitionx, pozitiony)
        jhan.pencolor(r.choice(image_colors).rgb)
        jhan.dot(20)


draw_hirst(7, 5)

my_screen.exitonclick()
