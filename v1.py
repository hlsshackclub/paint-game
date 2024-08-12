import ezdrawing

ezdrawing.open_window((800, 800))

last_mouse_pos = (0, 0)
while not ezdrawing.should_quit():
    mouse_pos = ezdrawing.get_mouse_pos()
    if 1 in ezdrawing.get_pressed_mouse_buttons():
        ezdrawing.draw_capped_line((0, 0, 0), last_mouse_pos, mouse_pos, 10)
    
    last_mouse_pos = mouse_pos
    
    ezdrawing.update()
ezdrawing.quit()