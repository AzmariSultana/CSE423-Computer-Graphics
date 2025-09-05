from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 
import time

speed, points = 60, 0
W_Width, W_Height = 500,500
stop, pause_symbol, isfrozen = True, False, False

diamond_x = 70
diamond_color = (1, 0, 0)
diamond_pos = [{
            "top_right_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x, "y2": 435},
            "top_left_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x-30, "y2": 435},
            "bottom_right_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x, "y2": 435},
            "bottom_left_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x-30, "y2": 435}},
            diamond_color] 

catcher_color = (1, 1, 1)
catcher_info = [{
    "base": {"x1": 15, "y1": 15, "x2": 90, "y2": 15},
    "left_diagonal": {"x1": 0, "y1": 30, "x2": 15 + 0, "y2": 15},
    "right_diagonal": {"x1": 90 + 0, "y1": 15, "x2": 110 + 0, "y2": 30},
    "above": {"x1": 0, "y1": 30, "x2": 110 + 0, "y2": 30}
}, catcher_color]

def draw_points(x, y, color):
    glColor3f(*color)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x 
    b = W_Height-y
    return (a,b)

def midpoint_line(x0, y0, x1, y1, zone, color):
    dx = x1 - x0
    dy = y1 - y0
    d = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)
    x = x0
    y = y0
    while x < x1:
        oz_x, oz_y = convertzoneM(x, y, zone)
        draw_points(oz_x , oz_y, color) 
        if d <= 0:
            d = d + incE
            x = x + 1
        else:
            d = d + incNE
            x = x + 1
            y = y + 1

    
def findzone(x1, y1, x2, y2):    
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6 
               
def convertzone0(x, y, zone):  
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (y, -x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (-y, x)
    elif zone == 7:
        return (x, -y)

def convertzoneM(x,y, zone):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (-y, x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (y, -x)
    elif zone == 7:
        return (x, -y)

def eight_way_symmetry(x1, y1, x2, y2, color = (1, 1, 0)):
    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convertzone0(x1, y1, zone)
    x2, y2 = convertzone0(x2, y2, zone)
    midpoint_line(x1, y1, x2, y2, zone, color)   

def catcher():
    global catcher_info
    for edge in catcher_info[0]:
        eight_way_symmetry(catcher_info[0][edge]["x1"], catcher_info[0][edge]["y1"], catcher_info[0][edge]["x2"], catcher_info[0][edge]["y2"], catcher_info[1])  

def diamond():
    global diamond_pos
    for edge in diamond_pos[0]:
        eight_way_symmetry(diamond_pos[0][edge]["x1"], diamond_pos[0][edge]["y1"], diamond_pos[0][edge]["x2"], diamond_pos[0][edge]["y2"], diamond_pos[1])

def specialKeyListener(key, x, y):
    global catcher_info, stop, isfrozen

    if stop and not isfrozen:
        if key == GLUT_KEY_RIGHT:
            if catcher_info[0]["right_diagonal"]["x2"] < 490:
                for edge in catcher_info[0]:
                    catcher_info[0][edge]["x1"] += 20
                    catcher_info[0][edge]["x2"] += 20
        
        elif key == GLUT_KEY_LEFT:
            if catcher_info[0]["left_diagonal"]["x1"] > 0:
                for edge in catcher_info[0]:
                    catcher_info[0][edge]["x1"] -= 20
                    catcher_info[0][edge]["x2"] -= 20

    glutPostRedisplay()

def has_collided(box1, box2):
    return (box1['x'] < box2['x'] + box2['width'] and
            box1['x'] + box1['width'] > box2['x'] and
            box1['y'] < box2['y'] + box2['height'] and
            box1['y'] + box1['height'] > box2['y'])

def draw_arrow():
    eight_way_symmetry(0, 470, 15,490, (0, 0, 1))
    eight_way_symmetry(0, 470, 15, 450, (0, 0, 1))
    eight_way_symmetry(0, 470, 50, 470, (0, 0, 1))

def draw_pause():
    global pause_symbol
    if pause_symbol and isfrozen:
        eight_way_symmetry(210, 450, 210, 490, (1, 1, 0))
        eight_way_symmetry(210, 450, 250, 470, (1, 1, 0))
        eight_way_symmetry(250, 470, 210, 490, (1, 1, 0))
    else:
        eight_way_symmetry(230, 450, 230, 490, (1, 1, 0))
        eight_way_symmetry(250, 450, 250, 490, (1, 1, 0))
  

def draw_cross():
    eight_way_symmetry(450, 450, 490, 490, (1, 0, 0))
    eight_way_symmetry(450, 490, 490, 450, (1, 0, 0))

def mouseListener(button, state, x, y):
    global pause_symbol, diamond_pos, catcher_info, diamond_x, diamond_color, stop, speed, points, isfrozen

    if button==GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            adj_x, adj_y = convert_coordinate(x, y)	

            #### Handle the Restart
            if 0 <= adj_x <= 50 and 450 <= adj_y <= 490:
                print("Starting Over")

                diamond_x = random.randint(30, 500)
                diamond_pos = [{
                            "top_right_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x, "y2": 435},
                            "top_left_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x-30, "y2": 435},
                            "bottom_right_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x, "y2": 435},
                            "bottom_left_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x-30, "y2": 435}},
                            diamond_color] 

                catcher_color = (1, 1, 1)
                catcher_info = [{
                    "base": {"x1": 20, "y1": 20, "x2": 100, "y2": 20},
                    "left_diagonal": {"x1": 0, "y1": 40, "x2": 20, "y2": 20},
                    "right_diagonal": {"x1": 100, "y1": 20, "x2": 120, "y2": 40},
                    "above": {"x1": 0, "y1": 40, "x2": 120, "y2": 40}
                }, catcher_color]

                points, speed, stop, isfrozen = 0, 60, True, False


            #### Handle cross button
            elif 450 <= adj_x <= 490 and 450 <= adj_y <= 490:
                print("GoodBye")
                glutLeaveMainLoop() 

            ## Play - Pause Handle
            elif 210 <= adj_x <= 250 and 450 <= adj_y <= 490:
                print("Play the game")
                pause_symbol = not pause_symbol
                isfrozen = not isfrozen    
            elif 230 <= adj_x <= 250 and 450 <= adj_y <= 490:
                print("Paused the game")
                pause_symbol = not pause_symbol
                isfrozen = not isfrozen

prev_time = time.time()
def animate():
    global diamond_pos, diamond_color, diamond_x, stop, speed, points, isfrozen, prev_time
    if stop and not isfrozen:

        curr_time = time.time()
        delta_time = curr_time - prev_time
        prev_time = curr_time
        movement = speed * delta_time

        catcher_box = {'x': catcher_info[0]["above"]["x1"], 'y': catcher_info[0]["above"]["y1"], 'width': 110, 'height': 15}
        diamond_box = {'x': diamond_pos[0]["bottom_left_edge"]["x2"], 'y': diamond_pos[0]["bottom_left_edge"]["y2"], 'width': 30, 'height': 30}

        if has_collided(diamond_box, catcher_box):
            diamond_x = random.randint(30, 500)
            diamond_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            diamond_pos = [{
                        "top_right_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x, "y2": 435},
                        "top_left_edge": {"x1": diamond_x-15, "y1": 450, "x2": diamond_x-30, "y2": 435},
                        "bottom_right_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x, "y2": 435},
                        "bottom_left_edge": {"x1": diamond_x-15, "y1": 420, "x2": diamond_x-30, "y2": 435}},
                        diamond_color] 

            print("Caught a Diamond!")
            points += 1
            speed += 2  # Or however much you want to increase after each catch
            print(f"Points: {points}")

        else:
            # Move diamond downward by `movement`
            for edge in diamond_pos[0]:
                diamond_pos[0][edge]["y1"] -= movement
                diamond_pos[0][edge]["y2"] -= movement
                if diamond_pos[0][edge]["y1"] < 0 and diamond_pos[0][edge]["y2"] < 0:
                    print("Game Over")
                    print("Your Score: ", points)
                    stop = False
                    catcher_info[1] = [1, 0, 0]
                    diamond_pos[1] = [0, 0, 0]

    glutPostRedisplay()
    time.sleep(0.01)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    catcher()
    diamond()
    draw_arrow()
    draw_pause()
    draw_cross()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Catch the Diamonds")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()