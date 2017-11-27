import pygame
import random
pygame.init()
screen_width=800
screen_height=500
white=(255,255,255)
red=(255,0,0)
green=(0,222,0)
blue=(0,0,111)
black=(0,0,0)
game_int=True
game_exit=False
snake_image=pygame.image.load('snake.png')
apple_image=pygame.image.load('apple.png')
pygame.display.set_icon(apple_image)
pygame.display.set_caption('Snake Game')
game_display = pygame.display.set_mode((screen_width,screen_height))
game_display.fill(white)
def button(color,x,y,w,h):
    pygame.draw.rect(game_display,color,[x,y,w,h])
def game_intro():
    global game_int,game_exit
    while game_int==True:
        pygame.draw.rect(game_display,black,[0,0,800,100])
        pygame.draw.rect(game_display,green,[250,700,60,20])
        msg_to_screen('***Snake x-x-x  Game***',30,white,100)
        msg_to_screen('Welcome To Snake Game',30,blue,300)
        msg_to_screen('You have to eat the apples as much as you can.',20,blue,400)
        msg_to_screen('The snake grows for each apple You eat.',20,blue,500)
        msg_to_screen('Eating Yourself or crossing the boundary is considered as OUT !',20,blue,600)
        button(green,250,700,60,20)
        button(blue,350,700,60,20)
        button(red,450,700,60,20)
        msg_to_screen('Press p to play the game or q to quit.',20,blue,700)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    game_int=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update()

def msg_to_screen(msg,size,color,height):
    font=pygame.font.Font('2086.ttf',size)
    text=font.render(msg,True,color)
    text_rect=text.get_rect()
    text_rect.center=(screen_width/2,height/2)
    game_display.blit(text,text_rect)
    
def game():
    direction='right'
    game_exit=False
    game_over=False
    block_width=20
    block_height=20
    apple_height=25
    apple_width=25
    lead_x=screen_width/2
    lead_y=screen_height/2
    lead_x_velocity=10
    lead_y_velocity=0
    change=10
    snakelength=1
    snake_list=[]
    apple_x=round(random.randrange(0,screen_width-apple_width))
    apple_y=round(random.randrange(100+apple_height,screen_height-apple_height))
    clock=pygame.time.Clock()
    score=0
    while not game_exit:
        while game_over==True:
            #game_display.fill(white)
            pygame.draw.rect(game_display,black,[0,0,800,100])
            msg_to_screen('***Snake x-x-x  Game***',30,white,100)
            msg_to_screen('Your Score Is %d'%score,25,green,400)
            msg_to_screen('GAME OVER !',25,blue,screen_height)
            msg_to_screen('Press c to try again or q to quit.',20,blue,screen_height+100)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exit=True
                    game_over=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        game()
                    if event.key==pygame.K_q:
                        game_over=False
                        game_exit=True
        game_display.fill(white)
        for xny in snake_list[:-1]:
            pygame.draw.rect(game_display,green,[xny[0],xny[1],block_width,block_height])
        pygame.draw.rect(game_display,black,[0,0,800,100])
        #pygame.draw.rect(game_display,red,[apple_x,apple_y,apple_width,apple_height])
        msg_to_screen('***Snake x-x-x  Game***',30,white,100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_velocity=-change
                    lead_y_velocity=0
                    direction='left'
                if event.key==pygame.K_RIGHT:
                    lead_x_velocity=change
                    lead_y_velocity=0
                    direction='right'
                if event.key==pygame.K_UP:
                    lead_y_velocity=-change
                    lead_x_velocity=0
                    direction='up'
                if event.key==pygame.K_DOWN:
                    lead_y_velocity=change
                    lead_x_velocity=0
                    direction='down'                    
        snake_head=[]
        lead_x+=lead_x_velocity
        lead_y+=lead_y_velocity
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if direction=='right':
            head=pygame.transform.rotate(snake_image,270)
        elif direction=='left':
            head=pygame.transform.rotate(snake_image,90)
        elif direction=='up':
            head=pygame.transform.rotate(snake_image,0)
        elif direction=='down':
            head=pygame.transform.rotate(snake_image,180)
        game_display.blit(head,(snake_list[-1][0],snake_list[-1][1]))
        game_display.blit(apple_image,[apple_x,apple_y])
        if len(snake_list)>snakelength:
            del snake_list[0]
        for eachsegment in snake_list[:-1]:
            if eachsegment==snake_list[-1]:
                game_over=True
        if lead_x>=apple_x and lead_x<apple_x+apple_width or lead_x+block_width>apple_x and lead_x+block_width<apple_x+apple_width:
            if lead_y>=apple_y and lead_y<apple_y+apple_height or lead_y+block_height>apple_y and lead_y+block_height<apple_y+apple_height:
                score+=1
                apple_x=round(random.randrange(0,screen_width-apple_width))
                apple_y=round(random.randrange(100,screen_height-apple_height))
                snakelength+=1
        if lead_x<0 or lead_x>=screen_width or lead_y<100 or lead_y>=screen_height:
            game_over=True
        msg_to_screen('Score: %d'%score,10,blue,250)
        clock.tick(20)
        pygame.display.update()
    pygame.quit()
    quit()
game_intro()
game()
