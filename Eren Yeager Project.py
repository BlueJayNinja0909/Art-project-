import turtle
import random

# Create the main drawing window (the canvas).
drawing_window = turtle.Screen()
drawing_window.setup(900, 700)                 # Set window size in pixels.
drawing_window.title("Eren Yeager Ocean by Doyun Lee")        # title of the window
drawing_window.colormode(255)                  # allows use of rgb colors. used for gradient

# basic configs
t = turtle.Turtle() # creates the turtle to draw
t.hideturtle() # hide the turtle to make image look clean
t.speed(0) # makes turtle fast. this is not needed due to tracer.
turtle.tracer(0, 0) #disables the animation of turtle drawing. update image at the end and is almost instant. SAVES LOTS OF TIME

# screen boundaries in pixels
left_side = -450
right_side = 450
top_side = 350
bottom_side = -350

# sky gradient. goes from top to horizon.
# this is the color used at the very top of screen. r=red g=green b=blue
top_color_r = 45
top_color_g = 135
top_color_b = 230

# this is the color used at the horizon its a ligher color.
bottom_color_r = 190
bottom_color_g = 245
bottom_color_b = 255
t.pensize(1) #very thin lines to make gradient as smooth as possible.

#draw horizontal line from the top to horizon which is y=10.
for y in range(top_side, 10, -1): # keep in mind top size is 350 from earlier. keep in mind the parentheses is (starting value, stop, step).
    # -1 step means move down 1. the 10 is a stop value.
    # progress measures how far we are from down. 0=top and 1 is bottom
    # This is the "blend factor" for gradient interpolation.
    progress = (top_side - y) / (top_side - 10) # top_side - y calculate how many pixel turtle moved down. top_side - 10 is total amount its taking.
    #top side= 350. bottom side=-350. divide beacuse i want to use this progress to calculate rgb color

    # current rgb value at vertical position.
    current_r = top_color_r + (bottom_color_r - top_color_r) * progress # top color is darkest. bottom color is value at horizon. (bottom_color_r - top_color_r) find how much red needs to change.
    current_g = top_color_g + (bottom_color_g - top_color_g) * progress
    current_b = top_color_b + (bottom_color_b - top_color_b) * progress

    # Clamp RGB values to [0,255]
    if current_r < 0: current_r = 0 # sets to lowest value if it accidently becomes negative.
    if current_r > 255: current_r = 255 # sets to highest value (255) if accidently become higher then limit
    if current_g < 0: current_g = 0 # sets to lowest value if it accidently becomes negative.
    if current_g > 255: current_g = 255  # sets to highest value (255) if accidently become higher then limit
    if current_b < 0: current_b = 0 # sets to lowest value if it accidently becomes negative.
    if current_b > 255: current_b = 255  # sets to highest value (255) if accidently become higher then limit

    # set color to draw
    t.pencolor(int(current_r), int(current_g), int(current_b))

    # draw 1 pixel horizantal line.
    t.penup()
    t.goto(left_side, y)
    t.pendown()
    t.forward(900)
    t.penup()

# horizon line to give contrast. pretty basic.
t.pencolor(10, 60, 150)
t.penup()
t.goto(left_side, 10)
t.pendown()
t.forward(900)
t.penup()

# OCEAN GRADIENT (HORIZON -> BOTTOM)
# setup for color at top and bottom of ocean. bottom is darker.
# top
ocean_top_r = 10
ocean_top_g = 190
ocean_top_b = 255
# bottom
ocean_bottom_r = 10
ocean_bottom_g = 55
ocean_bottom_b = 120

# basically the same thing as the sky one so i will not do comments. only different is progress increase as y value goes down.
for y in range(10, bottom_side, -1):
    # same as earlier
    progress = (10 - y) / (10 - bottom_side)

    # like the same thing as earlier.
    current_r = ocean_top_r + (ocean_bottom_r - ocean_top_r) * progress
    current_g = ocean_top_g + (ocean_bottom_g - ocean_top_g) * progress
    current_b = ocean_top_b + (ocean_bottom_b - ocean_top_b) * progress

    # same as earlier
    if current_r < 0: current_r = 0
    if current_r > 255: current_r = 255
    if current_g < 0: current_g = 0
    if current_g > 255: current_g = 255
    if current_b < 0: current_b = 0
    if current_b > 255: current_b = 255

    # choose pen color for the small horizontal line
    t.pencolor(int(current_r), int(current_g), int(current_b))

    # draw
    t.penup()
    t.goto(left_side, y)
    t.pendown()
    t.forward(900)
    t.penup()

# sun (basically 2 circles)
# yellow part
t.penup()
t.goto(320, 250)
t.pendown()
t.pencolor(255, 255, 230)
t.fillcolor(255, 255, 230)
t.begin_fill()
t.circle(55)
t.end_fill()
t.penup()

# white part
t.penup()
t.goto(320, 265)
t.pendown()
t.pencolor(255, 255, 255)
t.fillcolor(255, 255, 255)
t.begin_fill()
t.circle(35)
t.end_fill()
t.penup()

# small particle in the sky. like stars kinda
t.pensize(1) #keeps it thin and small

#the loop
for i in range(160):
    # randomize x y position in sky
    # random.randint(a, b) chooses a random number between a and b, inclduing both ends
    x = random.randint(left_side + 40, right_side - 40) # the plus minus 40 keeps it away from edge of screen.
    y = random.randint(150, top_side - 30)

    # Add small color variation. hardly noticiable.
    r = 230 + random.randint(-10, 10)
    g = 245 + random.randint(-10, 10)
    b = 255

    # prevents it from breaking. just like earlier.
    if r < 0: r = 0
    if r > 255: r = 255
    if g < 0: g = 0
    if g > 255: g = 255

    # set color to draw the partile
    t.pencolor(r, g, b)

    # draw a small line instead of a dot. this make it look textured and natural.
    t.penup()
    t.goto(x, y)
    t.pendown()
    length = random.randint(1, 3)
    t.forward(length)
    t.penup()

# big and small clouds
# big clouds  made of many circles including shadow and highlight.
for cloud_num in range(10): #make 10 big clouds.
    # randomize the center and size of the cloud
    x = random.randint(left_side + 140, right_side - 140)
    y = random.randint(180, 320)
    cloud_size = random.randint(35, 65) # NOT cloud center as i use offsets later on.

    # color for shadow part
    t.pencolor(190, 220, 255)
    t.fillcolor(190, 220, 255)

    # shadow part for big cloud
    for circle_num in range(6):
        # random x y offsets
        offset_x = random.randint(-cloud_size, cloud_size) #shift randomly left or right
        offset_y = random.randint(-cloud_size // 3, cloud_size // 3) - 8 # the double // is integer only so it remove any decimal. makes code simpler.
        # divide by 3 as clouds are wide not tall. -8 shift it down and makes it look more natural.
        # changes the radius
        radius = random.randint(cloud_size // 2, cloud_size) # makes each circle size different. the random int part removes perfect circles as that isnt realistic.

        # make it not go off screen
        new_x = x + offset_x # prevents clouds from being cut off from screen window.
        if new_x > right_side - 80: new_x = right_side - 80
        if new_x < left_side + 80: new_x = left_side + 80

        # make cloud stay over the horizon.
        new_y = y + offset_y
        if new_y < 10 + 55: new_y = 10 + 55 #55 to make it not go down too much.
        if new_y > top_side - 40: new_y = top_side - 40 # makes it not too high.

        # Draw a filled circle as part of the cloud.
        t.penup()
        t.goto(new_x, new_y - radius) # circle starts at the cordinate and goes up. by subtracting radius we get it to start where we want it to start.
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()

    # bright white circles on top. its lower then the shadow as we want the white to be ON TOP of shadow instead of other way around.
    t.pencolor(255, 255, 255)
    t.fillcolor(255, 255, 255)

    # SAME AS SHADOW BUT I CHANGED THE NUMBER A BIT TO MAKE IT LOOK BETTER.
    for circle_num in range(5):
        offset_x = random.randint(-cloud_size, cloud_size)
        offset_y = random.randint(-cloud_size // 3, cloud_size // 3)
        radius = random.randint(cloud_size // 2, cloud_size)

        new_x = x + offset_x
        if new_x > right_side - 80: new_x = right_side - 80
        if new_x < left_side + 80: new_x = left_side + 80

        new_y = y + offset_y
        if new_y < 10 + 55: new_y = 10 + 55
        if new_y > top_side - 40: new_y = top_side - 40

        t.penup()
        t.goto(new_x, new_y - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()

# Small clouds near the horizon for depth. pretty much the same code as big clouds.
for small_cloud_num in range(8):
    x = random.randint(left_side + 160, right_side - 160)
    y = random.randint(60, 100)
    size = random.randint(12, 18) # smaller compared to the 35,65 used in the bigger circle

    # shadow part for small cloud
    t.pencolor(190, 220, 255)
    t.fillcolor(190, 220, 255)

    for circle_num in range(4): # less amount for shadow as total amount of small cloud is smaller.
        # same idea
        offset_x = random.randint(-size, size)
        offset_y = random.randint(-size // 3, size // 3) - 4
        radius = random.randint(size // 2, size)

        # same idea
        new_x = x + offset_x
        if new_x > right_side - 80: new_x = right_side - 80
        if new_x < left_side + 80: new_x = left_side + 80

        # same idea
        new_y = y + offset_y
        if new_y < 10 + 55: new_y = 10 + 55
        if new_y > top_side - 40: new_y = top_side - 40

        # draw the shadow
        t.penup()
        t.goto(new_x, new_y - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()

    # bright part of cloud. basically same thing but smaller
    t.pencolor(255, 255, 255)
    t.fillcolor(255, 255, 255)

    for circle_num in range(3):
        offset_x = random.randint(-size, size)
        offset_y = random.randint(-size // 3, size // 3)
        radius = random.randint(size // 2, size)

        new_x = x + offset_x
        if new_x > right_side - 80: new_x = right_side - 80
        if new_x < left_side + 80: new_x = left_side + 80

        new_y = y + offset_y
        if new_y < 10 + 55: new_y = 10 + 55
        if new_y > top_side - 40: new_y = top_side - 40

        t.penup()
        t.goto(new_x, new_y - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.penup()

# shimmer in ocean. bascially sun reflection. easily the hardest part of the whole code. spent 6 hours on this on saturday. had outside help from parent and saji
# my dad wanted to use gaussian but that was too complicated to understand for me
num_lines = 360 # amount of horizantal lines

for ocean_row in range(num_lines): #repeats 360 times
    y = 10 - ocean_row # convert row number to y cordinate
    depth = ocean_row / 360  # how far down the ocean. near horizon is 0 while at bottom its 1. basically a slider from 0 to 1.
    # depth is super important. it allows me to scale brightness, length, and all that stuff smoothly depending on distance.

    # shimmer stroke counts depending on depth
    if depth < 0.3: #top 30 percent of ocean needs to look far away. draw 18 small shimmer line.
        reflections_this_line = 18
    elif depth < 0.6: # slightly less dense. 15 strokes.
        reflections_this_line = 15
    else: # closest to ocean needs less as i will make it bigger. so 12 is good number.
        reflections_this_line = 12

    # same length growth as before
    base_shimmer_length = 22 + (143) * depth
    # 22= smallest shimmer length. 143= biggest shimmer length. experimented with this a lot. keep in mind depth is bigger near bottom. this make shimmer longer near bototm.
    # its 22 plus 143* depth as if it was just 165 tiems depth there would be 0 shimmer at depth of 0.

    # draw multiple horizantal shimmer lines on a ocean row.
    for shimmer_line in range(reflections_this_line): # controls how many times the loop runs. keep in mind this changes depending on depth.

        # making most shimmer line appear near the sun.
        if random.random() < 0.78: # random.random() gives a random value from 0.0 to 1.0. this  means 78 percent of time put shimmer near the sun.
            spread = 140  # how far shimmer can go left AND right from the sun center x value.
            # n is like number. im choosing 4 random numbers from -140 to 140.
            n1 = random.randint(-spread, spread)
            n2 = random.randint(-spread, spread)
            n3 = random.randint(-spread, spread)
            n4 = random.randint(-spread, spread)
            x = 320 + (n1 + n2 + n3 + n4) // 4 # 320 is x positon of the sun. then i average the 4 random distance. this creates a realistic effect as if i add 1 random it will look pretty much the same. This make it so the data is slightly more concentrated in the center. 
                                               # basically chooses a x (horizontal) position for the shimmer.
        else:
            x = random.randint(left_side + 30, right_side - 30) # runs when not near the sun. this chooses a random x position witin screen bounds. adds wave thing and random shimmer everywhere.  

        # keeps shimmer inside screen range.
        if x > right_side - 30: x = right_side - 30
        if x < left_side + 30: x = left_side + 30

        # brightness of shimmer
        distance_from_sun = abs(x - 320) # abs = absolute value. distance can never be negative so we use this.
        brightness = 1.0 - distance_from_sun / 140 # keep in mind there is around 140 pixel randomness. distance/140 makes a number from around 0 to 1.
                                                    # then 1- this value makes closer to sun have higher brightness value then further.
        if brightness < 0: # ditance_from_sun might be bigger then 140. if that happens then brightness would be negative. that does not make sense.
                           # so -brighness turns to 0 brightness.
            brightness = 0

        # this make values more extreme. if its brighter (near sun) cubing it keeps it high. if its middle/low value, then cubing make it small.
        # result of this is super bright near the sun and quickly fade as shimmer x value goes away from center of sun.
        # i experimented with different powers like squaring and 4th power but 3rd power gives best balance.
        brightness = brightness * brightness * brightness  

        # shimmer color
        r = 185 + 60 * brightness # as you add more r and g value which would increase with high brightness, it become less blue and more white like.
        g = 225 + 40 * brightness
        b = 255

        # make color limit at 0 and 255 to avoid potential erros.
        if r < 0: r = 0
        if r > 255: r = 255
        if g < 0: g = 0
        if g > 255: g = 255

       # creates gaps in shimmer for natural effect.  
        gap_chance = 0.06 + 0.10 * depth # remember depth is 0 at horizon and 1 at bottom. at top 6 percent skip chance while 16 percent at bottom.
                                         # lower ocean y value = more gaps in shimmer
        if random.random() < gap_chance: # give decimal from 0.0 to 1.0. this make gap when random number land below gap_chance.
            continue # move on to the next iteration. if this happen it skips length pen size etc as there will be a gap.

        # how long each shimmer is. also this is random.
        length = int(base_shimmer_length * (0.6 + random.random()) * (0.7 + brightness))
        # base_shimme_length at horizon is smaller and at bottom its bigger. base= how long it should be originalaly. multiply by small variation so shimmer isnt identical.
        # also multiply by 0.7 plus brighness as closer to sun should be longer then further away. trying to replicate real life.

        # tiny position change so it doesnt look like perfect image. makes random just like real life.
        shimmer_x_offset = random.randint(-3, 3)
        shimmer_y_offset = random.randint(-1, 1)

        # changes thickness of shimmer depending on how far down the screen it is.
        if depth < 0.55:
            t.pensize(1) # top half ish of ocean uses smaller lines
        else: # anything lower uses bigger pen size.
            t.pensize(2)

        # draw the shimmer
        t.pencolor(int(r), int(g), int(b))
        t.penup()
        t.goto(x + shimmer_x_offset, y + shimmer_y_offset) # this is the randomness part
        t.pendown()
        t.setheading(0)
        t.forward(length) # random length of shimmer
        t.penup()

# Eren Yeager

# green cloak
t.pencolor(34, 61, 44)
t.fillcolor(34, 61, 44)
t.penup()
t.goto(-130, -360)
t.pendown()
t.begin_fill()
t.goto(-90, -145)
t.goto(-35, -140)
t.goto(0, -155)
t.goto(35, -140)
t.goto(90, -145)
t.goto(130, -360)
t.goto(-130, -360)
t.end_fill()
t.penup()

# darker gray part in the middle
t.pensize(4)
t.pencolor(220, 220, 220)
t.fillcolor(160, 160, 160)
t.penup()
t.goto(-52, -184)
t.pendown()
t.begin_fill()
t.goto(52, -184)
t.goto(44, -292)
t.goto(0, -330)
t.goto(-44, -292)
t.goto(-52, -184)
t.end_fill()
t.penup()

# lighter gray inner sheild ting
t.pensize(2)
t.pencolor(200, 200, 200)
t.fillcolor(210, 210, 210)
t.penup()
t.goto(-42, -196)
t.pendown()
t.begin_fill()
t.goto(42, -196)
t.goto(36, -286)
t.goto(0, -312)
t.goto(-36, -286)
t.goto(-42, -196)
t.end_fill()
t.penup()

# draw a line in the center to split left and right
t.pensize(4)
t.pencolor(220, 220, 220)
t.penup()
t.goto(0, -196)
t.pendown()
t.goto(0, -330)
t.penup()

# wings. not feather but the small shape at the bottom under the feathers. 
# left (blue)
t.pensize(3)
t.pencolor(220, 220, 220)
t.fillcolor(20, 70, 150)
t.penup()
t.goto(-36, -204)
t.pendown()
t.begin_fill()
t.goto(-13, -200)
t.goto(-15, -304)
t.goto(-33, -292)
t.goto(-42, -250)
t.goto(-36, -204)
t.end_fill()
t.penup()

# right (white)
t.pensize(3)
t.pencolor(220, 220, 220)
t.fillcolor(245, 245, 245)
t.penup()
t.goto(36, -204)
t.pendown()
t.begin_fill()
t.goto(13, -200)
t.goto(15, -304)
t.goto(33, -292)
t.goto(42, -250)
t.goto(36, -204)
t.end_fill()
t.penup()

# feathers. draws one feather lol. 
def draw_feather(points, fill_color, border_color, line_color): #make a function with parameters. 
    # each feather is a 4 corner polygon. here is what point is. its like
    # point 0 = top inner
    # point 1 = top outer
    # point 2 = bottom outer 
    # point 3 = bottom inner 
    # 0      1 this is what it is like. 
    # 3      2
    t.penup()
    t.goto(points[0]) #to to first
    t.pendown()
    # fill feather
    t.fillcolor(fill_color) # main color of body
    t.pencolor(border_color) # outline color
    t.pensize(1)
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[3])
    t.goto(points[0])
    t.end_fill()
    # brigher part on upper edge 
    t.pencolor(line_color)
    t.pensize(2)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.goto(points[1])
    t.penup()

# Colors
blue_fill   = (30, 90, 185)
blue_border = (185, 185, 185)
blue_line   = (235, 235, 235)
white_fill   = (250, 250, 250)
white_border = (190, 190, 190)
white_line   = (200, 200, 200)

# left side feathers. blue. this list is the cordinate. 
left_feathers = [
    [(-13.5, -208), (-44.5, -197), (-50.5, -205), (-15.5, -214)],
    [(-13.5, -215), (-42.4, -205), (-48.6, -213), (-15.5, -221)],
    [(-13.5, -222), (-40.3, -213), (-46.7, -221), (-15.5, -228)],
    [(-13.5, -229), (-38.2, -221), (-44.8, -229), (-15.5, -235)],
    [(-12.3, -236), (-32.4, -229), (-39.2, -237), (-14.3, -242)],  # pinch starts
    [(-12.3, -243), (-30.3, -237), (-37.3, -245), (-14.3, -249)],
    [(-12.3, -250), (-28.2, -245), (-35.4, -253), (-14.3, -256)],
    [(-12.3, -257), (-26.1, -253), (-33.5, -261), (-14.3, -263)],
    [(-12.3, -264), (-24.0, -261), (-31.6, -269), (-14.3, -270)],
    [(-13.5, -271), (-23.1, -268), (-30.9, -276), (-15.5, -277)],
    [(-13.5, -278), (-21.0, -275), (-29.0, -283), (-15.5, -284)],
    [(-13.5, -285), (-18.9, -282), (-27.1, -290), (-15.5, -291)],
]
for f in left_feathers: # f = each 4 cordinate feather. 
    draw_feather(f, blue_fill, blue_border, blue_line) # for each 4 cordinate feather in the list on top, run the draw function with color color given. 

# right side feathers. white. these are cords again 
right_feathers = [
    [(13.5, -208), (44.5, -197), (50.5, -205), (15.5, -214)],
    [(13.5, -215), (42.4, -205), (48.6, -213), (15.5, -221)],
    [(13.5, -222), (40.3, -213), (46.7, -221), (15.5, -228)],
    [(13.5, -229), (38.2, -221), (44.8, -229), (15.5, -235)],
    [(12.3, -236), (32.4, -229), (39.2, -237), (14.3, -242)],
    [(12.3, -243), (30.3, -237), (37.3, -245), (14.3, -249)],
    [(12.3, -250), (28.2, -245), (35.4, -253), (14.3, -256)],
    [(12.3, -257), (26.1, -253), (33.5, -261), (14.3, -263)],
    [(12.3, -264), (24.0, -261), (31.6, -269), (14.3, -270)],
    [(13.5, -271), (23.1, -268), (30.9, -276), (15.5, -277)],
    [(13.5, -278), (21.0, -275), (29.0, -283), (15.5, -284)],
    [(13.5, -285), (18.9, -282), (27.1, -290), (15.5, -291)],
]
for f in right_feathers: # same as the one on top. 
    draw_feather(f, white_fill, white_border, white_line)

# tail thing on bottom. the x shape
# blue one
t.fillcolor(30, 90, 185)
t.penup(); t.goto(-2, -285); t.pendown(); t.begin_fill()
t.goto(12, -305); t.goto(8, -310); t.goto(-4, -292); t.goto(-2, -285); t.end_fill()
# white one
t.fillcolor(250, 250, 250)
t.penup(); t.goto(2, -288); t.pendown(); t.begin_fill()
t.goto(-12, -309); t.goto(-8, -314); t.goto(4, -295); t.goto(2, -288); t.end_fill()

# Re-outline shield. makes final result look very crisp 
t.pensize(4)
t.pencolor(220, 220, 220)
t.penup()
t.goto(-52, -184)
t.pendown()
t.goto(52, -184)
t.goto(44, -292)
t.goto(0, -330)
t.goto(-44, -292)
t.goto(-52, -184)
t.penup()

# Eren's neck, hair, head
# neck
t.pencolor(210, 175, 145) 
t.fillcolor(210, 175, 145)
t.penup()
t.goto(-22, -145)
t.pendown()
t.begin_fill()
t.goto(-18, -100)
t.goto(18, -100)
t.goto(22, -145)
t.goto(0, -160)
t.goto(-22, -145)
t.end_fill()
t.penup()

# Draw the head silhouette (hair/shape) as a filled polygon.
t.pencolor(10, 8, 5)
t.fillcolor(10, 8, 5)
t.penup()
t.goto(0, -115)
t.pendown()
t.begin_fill()
#manual cordinates. this is like the head shape. 
t.goto(-35, -105)
t.goto(-45, -80)
t.goto(-40, -50)
t.goto(-20, -35)
t.goto(0, -32)
t.goto(20, -35)
t.goto(40, -50)
t.goto(45, -80)
t.goto(35, -105)
t.goto(15, -115)
t.goto(0, -110)
t.goto(-15, -115)
t.goto(0, -115) # Return to start to finish the head shape. 
t.end_fill()
t.penup()

# Draw hair strands as short random strokes for texture.
t.pensize(3)
t.pencolor(10, 8, 5) # same color as head

# Left-side hair strands.
t.penup()
t.goto(-40, -90)
t.pendown()
t.goto(-40 + random.randint(-5, 5), -105) # makes hair not perfectly straight
t.penup()
t.penup()
t.goto(-45, -70)
t.pendown()
t.goto(-45 + random.randint(-5, 5), -85)
t.penup()

# Right-side hair strands.
t.penup()
t.goto(40, -90)
t.pendown()
t.goto(40 + random.randint(-5, 5), -105)
t.penup()
t.penup()
t.goto(45, -70)
t.pendown()
t.goto(45 + random.randint(-5, 5), -85)
t.penup()

# Bottom hair strands.
t.penup()
t.goto(-15, -115)
t.pendown()
t.goto(-15 + random.randint(-5, 5), -130) # random direction
t.penup()
t.penup()
t.goto(15, -115)
t.pendown()
t.goto(15 + random.randint(-5, 5), -130) # random direction
t.penup()

# freedom text in middle. 
# black under
t.penup()
t.goto(0, -44) # lower by 4 pixels
t.pencolor(0, 0, 0)
t.write("FREEDOM", align="center", font=("ariel", 55, "bold"))
# white over
t.penup()
t.goto(0, -40)
t.pencolor(255, 255, 255)
t.write("FREEDOM", align="center", font=("ariel", 55, "bold"))


#makes it appear all at once and keep on screen
turtle.update()         
drawing_window.mainloop()