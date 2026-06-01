from graphics import Canvas
from time import sleep

    
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 405

def main():
    canvas=Canvas(CANVAS_WIDTH,CANVAS_HEIGHT) 
    #instructions to play
    canvas.create_text(130,60,text="WALL RALLY",font="Arial",font_size=30,color="blue")
    canvas.create_text(40,140,text="INSTRUCTIONS TO PLAY",font="Arial",font_size=18,color="red")
    canvas.create_text(20,190,text="Use LEFT and RIGHT arrow keys to move the racket(rectangle)",font="Arial",font_size=12,color="black")
    canvas.create_text(20,220,text="Keep the ball from reaching the ground",font="Arial",font_size=12,color="black")
    canvas.create_text(20,250,text="Each successful hit increases your score",font="Arial",font_size=12,color="black")
    canvas.create_text(20,280,text="Ball gets faster as your score increases",font="Arial",font_size=12,color="black")
    canvas.create_text(110,340,text="PRESS SPACE TO START",font="Arial",font_size=18,color="black")
    while True:
        keys=canvas.get_new_key_presses()
        if 'SPACE' in keys:
            canvas.clear()
            break
        sleep(0.05)
    background=canvas.create_rectangle(0,0,CANVAS_WIDTH,CANVAS_HEIGHT,"BLUE")


    #creating the racket
    left_x=150
    top_y=370
    right_x=240
    bottom_y=405
    racket=canvas.create_rectangle(left_x,top_y,right_x,bottom_y,'red','black')

    #creating the ball
    ball=canvas.create_oval(185,25,205,40,'yellow','black')

    #moving the ball
    dx=3
    dy=5

    #for score board
    score=0
    score_text=canvas.create_text(50,20,text="Score:",color="yellow")
    while True:
        
        keys=canvas.get_new_key_presses()
        canvas.move(ball,dx,dy)

         #ball moves 5px at a time and changes direction after collision with top or bottom.
        ball_y=canvas.get_top_y(ball)
        ball_height=canvas.get_object_height(ball)
        ball_bottom=ball_y+ball_height
        ball_x=canvas.get_left_x(ball)
        ball_width=canvas.get_object_width(ball)

        #collision with side wall
        if ball_x<=0:
            dx=-dx
        
        if ball_x+ball_width>= CANVAS_WIDTH:
            dx=-dx


        #racket characteristics
        racket_x=canvas.get_left_x(racket)
        racket_y=canvas.get_top_y(racket)
        racket_width= canvas.get_object_width(racket)

        #racket movement

        if 'LEFT_ARROW' in keys:
            if racket_x>0:
                canvas.move(racket,-10,0) #move racket to left
        
        if 'RIGHT_ARROW' in keys:
            if racket_x+racket_width<CANVAS_WIDTH:
                canvas.move(racket,10,0) #move racket to right
        
        if ball_bottom>=CANVAS_HEIGHT:
            game_over=canvas.create_text(110,190,text="GAME OVER",font="Arial",font_size=40,color="red")
            canvas.set_color(game_over,"red")
            final_score=canvas.create_text(160,250,"Final Score : " + str(score),font="Arial",font_size=20,color="yellow")
            canvas.set_color(final_score,"yellow")
            break

        if ball_y<=0:
            dy=-dy
        sleep(0.05)


        #collision of racket and ball
        if ball_bottom>=racket_y:
            if racket_x<=ball_x<=racket_x+racket_width:
                dy=-dy
                score+=1
                canvas.change_text(score_text,"score:"+str(score))
                if score % 5 == 0:
                    if dy>0:
                        dy+=1
                    else:
                        dy-=1
        

       


        
if __name__ == '__main__':
    main()
