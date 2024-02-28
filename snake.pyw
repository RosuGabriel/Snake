#%%
import pygame
import random

# raeding high score from file
f = open('hscore.txt','r')
high_score = int(f.read())
f.close()

# colors and screen size
fullScreen = False
white = (255,255,255)
green = (25,138,66)
red = (240,42,28)
yellow = (239,252,57)
black = (4,40,63)
blue = (12,120,190)
navy = (9,93,148)
width = 1280
height = 720
ex = ''

# pygame settings
pygame.init()
pygame.RESIZABLE
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption('python snake game')
clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15
message_font = pygame.font.Font( 'PixeloidSans-JR6qo.ttf', 25)
score_font = pygame.font.SysFont('ubuntu', 16)

# instructiions and score
def print_score(score):
    text = score_font.render('Score: '+ str(score), True, white )
    text2 = score_font.render('High score: '+str(high_score), True, white )
    text3 = score_font.render('iesire esc', True, white )
    text4 = score_font.render('restart r', True, white )
    text5 = score_font.render('fullscreen f', True, white )
    
    SCREEN.blit(text, [0,0])
    SCREEN.blit(text2, [0,15])
    SCREEN.blit(text3, [1220,0])
    SCREEN.blit(text4, [1230,15])
    SCREEN.blit(text5, [1211,30])
    


# drawing the snake
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels[-1:-3:-1]:   
        pygame.draw.rect(SCREEN, black, [pixel[0], pixel[1], snake_size, snake_size])
   
    for pixel in snake_pixels[-3::-2]:
        pygame.draw.rect(SCREEN, blue, [pixel[0], pixel[1], snake_size, snake_size])
   
    for pixel in snake_pixels[-4::-2]:
        pygame.draw.rect(SCREEN, navy, [pixel[0], pixel[1], snake_size, snake_size])
    
        

# main game loop
def run():
    # global variables
    global ex
    global fullScreen
    global snake_speed
    global high_score
    
    # local variables of the game
    game_over = False
    game_close = False
    x = width / 2
    y = height / 2
    EXx = 0
    EXy = 0
    speedx = 0
    speedy = 0
    snake_pixels = []
    snake_lenght = 1

    # target position
    xtarget = round(random.randrange(0,width-snake_size)/ 10.0) * 10.0
    ytarget = round(random.randrange(0,height-snake_size)/ 10.0) * 10.0
    
    # game loop
    while not game_over:

        # game over screen
        while game_close:
            global high_score
            global SCREEN
        
            # actualization of high score
            if snake_lenght-1 > high_score:
                high_score = snake_lenght - 1
                f = open('hscore.txt','w')
                f.write(str(high_score))
                f.close()
            
            for event in pygame.event.get():
              
                if event.type == pygame.KEYDOWN:
              
                    if event.key == pygame.K_ESCAPE:
                        game_over= True
                        game_close= False    
              
                    if event.key == pygame.K_r:
                        snake_speed = 15
                        ex = ''
                        run()
              
                    if event.key == pygame.K_f:  
              
                        if not fullScreen:
                            SCREEN = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
                            pygame.display.update() 
                            fullScreen = True
                        else:
                            SCREEN = pygame.display.set_mode((width, height))
                            pygame.display.update()    
                            fullScreen = False
              
                if event.type  == pygame.QUIT:
                    game_close = True
                    game_over = True
                    pygame.quit()
                    quit()    
                        
            SCREEN.fill(green)
            game_over_message = message_font.render("Game Over", True, black)
            text = game_over_message.get_rect(center=(width/2,height/2))
            SCREEN.blit(game_over_message, text)
            print_score(snake_lenght-1)
            pygame.display.update()
            
        # event handling
        for event in pygame.event.get():
            
            if event.type  == pygame.QUIT:
                game_over= True
            
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_f:  
                
                    if not fullScreen:
                        SCREEN = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
                        pygame.display.update() 
                        fullScreen = True
                    else:
                        SCREEN = pygame.display.set_mode((width, height))
                        pygame.display.update()    
                        fullScreen = False
            
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False    
            
                if event.key == pygame.K_r:
                    snake_speed = 15
                    ex = ''
                    run()
            
                if EXx != x or EXy != y:
            
                    if event.key == pygame.K_LEFT and ex != 'right':
                        speedx = -snake_size
                        speedy = 0
                        ex = 'left' 
                        EXx = x
                        EXy = y
            
                    if event.key == pygame.K_RIGHT and ex != 'left':
                        speedx = snake_size
                        speedy = 0
                        ex = 'right'
                        EXx = x
                        EXy = y
            
                    if event.key == pygame.K_DOWN and ex != 'up':
                        speedx = 0
                        speedy = snake_size
                        ex = 'down'
                        EXx = x
                        EXy = y
            
                    if event.key == pygame.K_UP and ex != 'down':
                        speedx = 0
                        speedy = -snake_size
                        ex = 'up'
                        EXx = x
                        EXy = y
        
        # game over conditions
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += speedx    
        y += speedy
        
        SCREEN.fill(green)
        pygame.draw.rect(SCREEN, red, [xtarget, ytarget, snake_size, snake_size])
        snake_pixels.append([x,y])
        
        if len(snake_pixels)>snake_lenght:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close=True
                
        draw_snake(snake_size, snake_pixels)
        print_score(snake_lenght-1)
        
        pygame.display.update()
        
        if x == xtarget and y == ytarget:
            xtarget= round(random.randrange(0,width-snake_size) / 10.0) * 10.0
            ytarget= round(random.randrange(0,height-snake_size) / 10.0) * 10.0
            snake_lenght += 1
            snake_speed += 1
        
        clock.tick(snake_speed)
    
    pygame.display.quit()
    pygame.quit()
    quit()



# running the game         
run()
