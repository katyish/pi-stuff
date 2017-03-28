from blinkt import set_clear_on_exit, set_brightness, set_pixel, show

set_clear_on_exit()
set_brightness(0.1)

# light up in rainbow colours.  Yes, very exciting...

while True:
        set_pixel(0, 255, 0, 0) #red
        set_pixel(1, 255, 128, 0) #orange
        set_pixel(2, 255, 255, 0) #yellow
        set_pixel(3, 0, 255, 0) #green
        set_pixel(4, 0, 255, 255) #cyan
        set_pixel(5, 0, 0, 255) #blue
        set_pixel(6, 128, 0, 255) #purple
        set_pixel(7, 255, 0, 255) #pink

        show()