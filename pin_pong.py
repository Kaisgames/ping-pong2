from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    
display.set_caption('Ping Pongggggg')
back = (220, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('back2.png'), (win_width, win_height))

mixer.init()
mixer.music.load('musik.ogg')
mixer.music.play()

game = True
finish = False
clock = time.Clock()
FPS = 60
plot1 = Player('plate2.png', 30, 200, 4, 50, 150)
plot2 = Player('plate3.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball2.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0, 0))
        plot1.update_l()
        plot2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(plot1, ball) or sprite.collide_rect(plot2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        plot1.reset()
        plot2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)