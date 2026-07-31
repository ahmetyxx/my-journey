from prettytable import PrettyTable
# from turtle import Turtle, Screen

# kenji= Turtle()
# kenji.shape("turtle")
# kenji.color("green","cyan1")
# kenji.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


my_table= PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
my_table.add_column("Type",["Electric","Water","Fire"])
my_table.align="l"
print(my_table)
