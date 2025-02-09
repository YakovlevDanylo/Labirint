from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_s] and self.rect.y > 0:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.x < 430:
            self.rect.y -= self.speed

        super().update(screen)


window = display.set_mode((700, 500))
display.set_caption("Лабіринт")

background = transform.scale(image.load("background.jpg"), (700, 500))
player = Player("cat.jpg", 100, 400, 70, 70, 5)


timer = time.Clock()
fps = 60

end_game = False
finished = False

while not end_game:
    for e in event.get():
        if e.type == QUIT:
            end_game = True

    if not finished:
        window.blit(background, (0,0))

        player.update(window)


        display.update()
        timer.tick(fps)
