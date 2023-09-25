from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open canvus(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
idle = load_image('Idle.png')
run = load_image('Run.png')
walk = load_image('Walk.png')

x, y =TUK_WIDTH //2 , TUK_HEIGHT //2
Idle = true
frame = 0

while Idle:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT)
    update_canvas()
    frame= (frame + 1) % 5
    delay(0.05)

close_canvas()