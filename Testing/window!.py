#import library
import arcade

#make window
arcade.open_window(600, 600, "Drawing no1")

#set background
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

#ready to draw
arcade.start_render()

#draawwwwwww

#grass using left-right-top-bottom
arcade.draw_lrtb_rectangle_filled(0, 599,300,0, arcade.csscolor.GREEN)
#tree trunk using centerx-centery-width-height
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

#another tree, ellipse top this time
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

#parasol?
arcade.draw_rectangle_filled(300, 300, 10, 60, arcade.csscolor.WHITE)
arcade.draw_arc_filled(300, 330, 50, 20, arcade.csscolor.DARK_MAGENTA, 0, 180)

#sun
arcade.draw_circle_filled(400, 500, 25, arcade.color.YELLOW)
#rays up down left right
arcade.draw_line(400, 500, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 400, 450, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 350, 500, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 450, 500, arcade.color.YELLOW, 3)
#rays rightup rightdown leftdown leftup
arcade.draw_line(400, 500, 435, 535, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 435, 465, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 365, 465, arcade.color.YELLOW, 3)
arcade.draw_line(400, 500, 365, 535, arcade.color.YELLOW, 3)

#stop draw
arcade.finish_render()

#at the end to keep the window open when the lines of code are done
arcade.run()