# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player
from enemy import Enemy
# РАЗМЕРЫ ОКОШКА
WIDTH = 500
HEIGHT = 300

FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


player = Player("./capibara.png",100,120, 200,200)

enemyGroup = pygame.sprite.Group()
def spawnEnemy():
    enemy = Enemy("./zombie.png" , width=rd(20,50),height=rd(20,50),x=rd(0,WIDTH),y=rd(0,200))
    enemyGroup.add(enemy)

    #Запускаем Спавн Противников
for i in range(5):
   spawnEnemy()



# TODO Добавить второго противника, сделать следование за игроком

# Цикл игры
running = True
while running:

    screen.fill(WHITE)
    # pygame.draw.rect(screen, GREEN,(200,200,50,20))

  
    player.draw(screen)
    player.movement()
    # Держим цикл на правильной скорости
    
    for enemy in enemyGroup:
     enemy.draw(screen)
     enemy.follow(player)
 

    # ОТСЛЕЖИВАЕМ СТОЛКНОВЕНИЕ С ИГРОКОМ
     if pygame.sprite.spritecollideany(player,
    enemyGroup):
      print("СТОЛКНОВЕНИЕ, СОЖРАЛИ")
      Player.hp -=2
      if player.hp <= 0:
          print("ГЕЙМ ОВЕР")
          running = False

    clock.tick(FPS)
    pygame.display.update()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()


# домашка 21.12.2024
# TODO Сделать движение вверх-вниз через клавиши, сделать проверки на пересечение верхней границы, нижней, и левой границ