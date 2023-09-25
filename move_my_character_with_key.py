from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
idle = load_image('Idle.png')
run = load_image('Run.png')
walk = load_image('Walk.png')

def handle_events():
    global State
    global Stay, Running, Walking
    global dirx, diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            State = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Stay = False
                Running = True
                dirx += 1
            elif event.key == SDLK_LEFT:
                Stay = False
                Running = True
                dirx -= 1
            elif event.key == SDLK_UP:
                Stay = False
                Walking = True
                diry += 1
            elif event.key == SDLK_DOWN:
                Stay = False
                Walking = True
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                State = False
        elif event.type == SDL_KEYUP:
            Running = False
            Walking = False
            Stay = True
            if event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1


x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
State = True
Stay = True
Running = False
Walking = False
frame = 0
dirx = 0
diry = 0

while State:
    if Stay:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT//2)
        idle.clip_draw(frame* 100,0,85, 100, x, y, 150, 150)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 3
        delay(0.3)
    if Running:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        run.clip_draw(frame * 100, 0, 85, 100, x, y, 150, 150)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 5
        x += dirx * 5
        if x > 1280 - 85:
            x= 1280-85
        if x < 0 + 85:
            x = 0 + 85
        delay(0.1)
    if Walking:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        walk.clip_draw(frame * 100, 0, 85, 100, x, y, 150, 150)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 4
        y += diry * 5
        if y > 1024 - 50 :
            y = 1024- 50
        if y < 0 + 100:
             y = 0 + 100
        delay(0.1)

close_canvas()