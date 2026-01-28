# a116_buggy_image_BA_fixed.py
# This program draws a spider with 8 correctly placed legs

import turtle as trtl

# Create the turtle
spider = trtl.Turtle()
spider.speed(0)

# Draw the spider body
spider.pensize(40)
spider.circle(20)


number_of_legs = 8            
leg_length = 70
angle_between_legs = 360 / number_of_legs  


spider.pensize(5)



count = 0
while count < number_of_legs:
    spider.penup()
    spider.goto(0, 20)        
    spider.setheading(angle_between_legs * count)
    spider.pendown()
    spider.forward(leg_length)
    count = count + 1

# Finish
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
