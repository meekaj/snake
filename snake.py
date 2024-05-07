import turtle as t
import random as rd

def setup_window():
    t.bgcolor('orange')
    t.title("Turtle Snake Game")

def setup_snake():
    snake.shape('square')
    snake.color('black')
    snake.speed(0)
    snake.penup()
    snake.hideturtle()

def setup_leaf():
    leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
    t.register_shape('leaf', leaf_shape)
    leaf.shape('leaf')
    leaf.color('green')
    leaf.penup()
    leaf.hideturtle()

def setup_scoreboard():
    score_turtle.hideturtle()
    score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = snake.pos()
    return x < left_wall or x > right_wall or y > top_wall or y < bottom_wall

def game_over():
    snake.color('orange')
    leaf.color('orange')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))
    t.onkey(start_game, 'space')

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 70
    y = (t.window_height() / 2) - 70
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

def display_instructions():
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.hideturtle()
    text_turtle.goto(0, 20) #higher for first line
    text_turtle.write('Press Space to Start!', align='center', font=('Arial', 30, 'normal'))
    text_turtle.goto(0, -40)
    text_turtle.write('Use arrow keys to control', align='center', font=('Arial', 30, 'normal'))

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    text_turtle.clear() 
    score_turtle.clear()

    snake_speed = 2
    snake_length = 3
    score = 0

    #snake appearance and position
    snake.shapesize(1, snake_length, 1)
    snake.color('black')  
    snake.penup()
    snake.goto(0, 0) 
    snake.showturtle()

    display_score(score)
    place_leaf()
    
    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            place_leaf()
            snake_length += 1
            snake.shapesize(1, snake_length, 1)
            snake_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def bind_keys():
    t.onkey(start_game, 'space')
    t.onkey(move_up, 'Up')
    t.onkey(move_right, 'Right')
    t.onkey(move_down, 'Down')
    t.onkey(move_left, 'Left')

def move_up():
    if snake.heading() != 270:
        snake.setheading(90)

def move_down():
    if snake.heading() != 90:
        snake.setheading(270)

def move_left():
    if snake.heading() != 0:
        snake.setheading(180)

def move_right():
    if snake.heading() != 180:
        snake.setheading(0)

def main():
    setup_window()
    setup_snake()
    setup_leaf()
    setup_scoreboard()
    display_instructions()
    bind_keys()
    t.listen()
    t.mainloop()

if __name__ == '__main__':
    snake = t.Turtle()
    leaf = t.Turtle()
    text_turtle = t.Turtle()
    score_turtle = t.Turtle()
    game_started = False
    main()