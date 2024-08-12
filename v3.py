import ezdrawing

color = (0, 0, 0)
def select_color():
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
def select_size():
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

tool = "pen"
def select_tool():
    global tool
    pressed_keys = ezdrawing.get_pressed_keys()
    if "1" in pressed_keys:
        tool = "pen"
    if "2" in pressed_keys:
        tool = "line"
    if "3" in pressed_keys:
        tool = "rect"
    if "4" in pressed_keys:
        tool = "ellipse"

last_mouse_pos = (0, 0)
def use_pen():
    global size, color, last_mouse_pos
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        ezdrawing.draw_capped_line(color, last_mouse_pos, mouse_pos, size)
    
    last_mouse_pos = mouse_pos

line_start_pos = None
def use_line():
    global size, color, line_start_pos
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        if line_start_pos == None:
            line_start_pos = mouse_pos
        else:
            ezdrawing.undo()
        ezdrawing.draw_line(color, line_start_pos, mouse_pos, size)
    else:
        line_start_pos = None

rect_start_pos = None
def use_rect():
    global size, color, rect_start_pos
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        if rect_start_pos == None:
            rect_start_pos = mouse_pos
        else:
            ezdrawing.undo()
        top_left = (min(rect_start_pos[0], mouse_pos[0]), min(rect_start_pos[1], mouse_pos[1]))
        bottom_right = (max(rect_start_pos[0], mouse_pos[0]), max(rect_start_pos[1], mouse_pos[1]))
        ezdrawing.draw_rect(color, top_left, bottom_right)
    else:
        rect_start_pos = None

ellipse_start_pos = None
def use_ellipse():
    global size, color, ellipse_start_pos
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        if ellipse_start_pos == None:
            ellipse_start_pos = mouse_pos
        else:
            ezdrawing.undo()
        top_left = (min(ellipse_start_pos[0], mouse_pos[0]), min(ellipse_start_pos[1], mouse_pos[1]))
        bottom_right = (max(ellipse_start_pos[0], mouse_pos[0]), max(ellipse_start_pos[1], mouse_pos[1]))
        ezdrawing.draw_ellipse(color, top_left, bottom_right)
    else:
        ellipse_start_pos = None

ezdrawing.open_window((800, 800))

last_mouse_pos = (0, 0)
while not ezdrawing.should_quit():
    if not 1 in ezdrawing.get_pressed_mouse_buttons():
        select_color()
        select_size()
        select_tool()
    
    if tool == "pen":
        use_pen()
    elif tool == "line":
        use_line()
    elif tool == "rect":
        use_rect()
    else:
        use_ellipse()
    
    if "x" in ezdrawing.get_pressed_keys():
        ezdrawing.save("x.png")
    
    ezdrawing.update()
ezdrawing.quit()