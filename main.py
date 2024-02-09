import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")  # Set the title of the screen

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  # Set the background image

states_data = pandas.read_csv("50_states.csv")  # Read the data
all_states = states_data.state.to_list()
guessed_states = []
textinput_title = "Guess the State"

while len(guessed_states) < len(all_states):
    # Get the user's answer
    answer_state = screen.textinput(title=textinput_title, prompt="What's another state's name?").title()

    if answer_state.lower() == "exit":
        # Generate a .csv file that contains the missed states
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Check for the answer in the data
    state = states_data[states_data.state == answer_state]
    if not state.empty:  # If it exists
        guessed_states.append(state.state.item())
        textinput_title = f"{len(guessed_states)}/{len(all_states)} States Correct"  # Show the

        # Write the state on the map
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(state.x.item()), state.y.iloc[0])
        state_turtle.write(state.state.item())
