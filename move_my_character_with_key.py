from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
idle = load_image('Idle.png')
run = load_image('Run.png')
walk = load_image('Walk.png')

x, y = TUK_WIDTH //2 , TUK_HEIGHT //2
Idle = True
frame = 0

def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Idle = False



while Idle:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT//2)
    idle.clip_draw(frame* 100,0,100, 100, 400, 400)
    update_canvas()
    frame= (frame + 1) % 4
    delay(0.3)

close_canvas()