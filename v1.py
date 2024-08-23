import ezdrawingtk

ezdrawingtk.open_window((800, 800))

last_mouse_pos = (0, 0)
while not ezdrawingtk.should_quit():
    mouse_pos = ezdrawingtk.get_mouse_pos()
    if 1 in ezdrawingtk.get_pressed_mouse_buttons():
        ezdrawingtk.draw_capped_line((0, 0, 0), last_mouse_pos, mouse_pos, 10)
    
    last_mouse_pos = mouse_pos
    
    ezdrawingtk.update()