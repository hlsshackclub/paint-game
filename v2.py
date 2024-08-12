import ezdrawing

color = (0, 0, 0)
def selectColor():
    global color
    pressed_keys = ezdrawing.get_pressed_keys()
    if "q" in pressed_keys:
        color = (0, 0, 0)
    elif "w" in pressed_keys:
        color = (255, 255, 255)
    elif "e" in pressed_keys:
        color = (255, 0, 0)
    elif "r" in pressed_keys:
        color = (0, 255, 0)
    elif "t" in pressed_keys:
        color = (0, 0, 255)

size = 1
def selectSize():
    global size
    pressed_keys = ezdrawing.get_pressed_keys()
    if "a" in pressed_keys:
        size = 1
    if "s" in pressed_keys:
        size = 2
    if "d" in pressed_keys:
        size = 4
    if "f" in pressed_keys:
        size = 8
    if "g" in pressed_keys:
        size = 16
    if "h" in pressed_keys:
        size = 32
    if "j" in pressed_keys:
        size = 64
    if "k" in pressed_keys:
        size = 128

ezdrawing.open_window((800, 800))

last_mouse_pos = (0, 0)
while not ezdrawing.should_quit():
    selectColor()
    selectSize()
    
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        ezdrawing.draw_capped_line(color, last_mouse_pos, mouse_pos, size)
    
    last_mouse_pos = mouse_pos
    
    ezdrawing.update()
ezdrawing.quit()