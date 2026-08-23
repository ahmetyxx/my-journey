from turtle import Screen, Turtle
import turtle
import pandas as pd

my_screen=Screen()
my_screen.title("U.S states")
image="U.S states/blank_states_img.gif"
my_screen.addshape(image)


jhan=Turtle()
jhan.shape(image)
drawer=Turtle()
drawer.hideturtle()
drawer.penup()

state_names=pd.read_csv("U.S states/50_states.csv").state
states=pd.read_csv("U.S states/50_states.csv")




correct_states=[]


is_game_on = True

while is_game_on:

    answer_state= my_screen.textinput(f"{len(correct_states)}/50 states correct","what's next state?").lower()
    
    if answer_state not in correct_states:
        xy_pos=states.loc[states["state"].str.lower()==answer_state,["x","y"]]
            
        if not xy_pos.empty:
            
            correct_states.append(answer_state)
            print(correct_states)
            xpos=xy_pos["x"].iloc[0]
            ypos=xy_pos["y"].iloc[0]
            drawer.goto(xpos,ypos)
            drawer.write(answer_state)

my_screen.mainloop()
