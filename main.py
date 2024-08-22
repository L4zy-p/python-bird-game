import pygame
import configs
import asset
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False

asset.load_sprites()
asset.load_audios()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    # ทำให้ backgroung ที่มีรูป เดิมไหลมาต่อกัน
    Background(0, sprites)
    Background(1, sprites)

    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = create_sprites()

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            # เรียก pipe ทุกครั้งที่มี event
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)
                
                # กด q เพื่อเริ่มใหม่
            if event.key == 113 and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_message, score = create_sprites()
               
        
        bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen)

    if gamestarted and not gameover: 
        sprites.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        gamestarted = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)
        asset.play_audio("hit")
        
    
    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            asset.play_audio("point")

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()