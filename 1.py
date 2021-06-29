import pygame

pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Tururu Uzubaru')


x = 250
y = 250
width = 40
height = 120
vel = 20

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500-width-vel:
        x += vel    

    if not isJump:
        if keys[pygame.K_UP] and y > vel:
                y -= vel
        if keys[pygame.K_DOWN] and y < 500-height-vel:
                y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= neg * jumpCount ** 2 /2

            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))    
    pygame.draw.rect(win, (102,63,48), (x,y,width,height))
    pygame.display.update()
     


pygame.quit()   