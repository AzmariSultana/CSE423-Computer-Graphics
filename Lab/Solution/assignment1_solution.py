#Task1
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(view,view,view,0)
    glLoadIdentity()
    iterate()
    buildHome()
    rainFall()
    glutSwapBuffers()
width,height=500,500
view=0.8

rain, Angle=[],0.0
for i in range(200):
    a = random.randint(0, width)
    b = random.randint(0,height)
    rain.append([a, b])

def buildHome():
    homeRoof()
    homeBase()
    homeDoor()
    homeWindow1()
    homeWindow2()
    

def homeRoof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.612, 0.459, 0.02)
    glVertex2f(60,220)
    glVertex2f(410,220)
    glVertex2f(235,320)
    glVertex2f(60,220)
    glVertex2f(410,220)
    glVertex2f(235,320)
    glEnd()

def homeBase():
    glBegin(GL_TRIANGLES)
    glColor3f(0.671, 0.624, 0.075)

    glVertex2f(90,90)
    glVertex2f(380,90)
    glVertex2f(90,220)
    glVertex2f(90,90)
    glVertex2f(380,90)
    glVertex2f(90,220)

    glVertex2f(380,90)
    glVertex2f(90,220)
    glVertex2f(380,220)
    glVertex2f(380,90)
    glVertex2f(90,220)
    glVertex2f(380,220)
    glEnd()

def homeDoor():
    glBegin(GL_TRIANGLES)
    glColor3f(0.176, 0.059, 0.478)
   
    glVertex2f(200, 90) 
    glVertex2f(260, 90) 
    glVertex2f(260, 170) 
    glVertex2f(200, 90) 
    glVertex2f(260, 90) 
    glVertex2f(260, 170) 
    
    glVertex2f(200, 90) 
    glVertex2f(260, 170) 
    glVertex2f(200, 170) 
    glVertex2f(200, 90) 
    glVertex2f(260, 170) 
    glVertex2f(200, 170)
    glEnd()


def homeWindow1():
    glBegin(GL_TRIANGLES)
    glColor3f(0.294, 0.184, 0.569)
   
    glVertex2f(120, 140) 
    glVertex2f(120, 190) 
    glVertex2f(160, 190)
    glVertex2f(120, 140) 
    glVertex2f(120, 190) 
    glVertex2f(160, 190)
  
    
    glVertex2f(160, 190)
    glVertex2f(160, 140) 
    glVertex2f(120, 140) 
    glVertex2f(160, 190)
    glVertex2f(160, 140) 
    glVertex2f(120, 140) 
    
    glEnd()

def homeWindow2():
    glBegin(GL_TRIANGLES)
    glColor3f(0.294, 0.184, 0.569)
   
    glVertex2f(310, 140) 
    glVertex2f(310, 190) 
    glVertex2f(350, 190)
    glVertex2f(310, 140) 
    glVertex2f(310, 190) 
    glVertex2f(350, 190)
  
    
    glVertex2f(350, 190)
    glVertex2f(350, 140) 
    glVertex2f(310, 140) 
    glVertex2f(350, 190)
    glVertex2f(350, 140) 
    glVertex2f(310, 140) 
    
    glEnd()
    
def keyboardListener(key, a, b):

    global view
    if key==b'n':
        view=max(0.2,view-0.1)
        
    if key==b'd':
        view=min(0.8,view+0.1)
    glutPostRedisplay()

def rainFall():
    global rain, Angle
    glColor3f(0.396, 0.722, 0.831)
    glBegin(GL_LINES)
    for drop in rain:
        a, b = drop
        glVertex2f(a, b)
        glVertex2f(a + Angle, b - 30)
    glEnd()

def animation():
    global rain
    for drop in rain:
        drop[0] += Angle
        drop[1] -= 2
        if drop[0] > width:
            drop[0] = drop[0] - width
        elif drop[0] < 0:
            drop[0] = width + drop[0]

        if drop[1] < 0:
            drop[0] = random.uniform(0, width)
            drop[1] = height
    glutPostRedisplay()

def specialKeyListener(key, a, b):
    global Angle
    if key == GLUT_KEY_RIGHT and Angle < 5:
        Angle += 8
    elif key == GLUT_KEY_LEFT and Angle > -5:
        Angle -= 8
    glutPostRedisplay()

    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Azmari's sweet home")
glutDisplayFunc(showScreen)
glutIdleFunc(animation)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()


#Task2
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# points = []
# speed = 1
# pause = False
# blink = False
# ball_size = 10
# direction_color = []
# Width, Height = 800, 800


# def convert_coordinate(x, y):
#     global Width, Height
#     a = x - (Width / 2)
#     b = (Height / 2) - y
#     return a, b

# def mouseListener(button, state, x, y):
#     global points, direction_color, pause, blink
#     if pause== True:
#         return
#     if pause== False:
#          if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#           point = convert_coordinate(x, y)
#           if -300 < point[0] < 300 and -300 < point[1] < 300:
#             points.append(point)
#             color = [random.random(), random.random(), random.random()]
#             tempX = random.randint(0, 2)
#             if tempX == 0:
#                 stepX = -1*speed
#             else:
#                 stepX = 1*speed
#             tempY = random.randint(0, 2)
#             if tempY == 0:
#                 stepY = -1*speed
#             else:
#                 stepY = 1*speed
#             direction = (stepX, stepY)
#             tempList = [direction, color]
#             direction_color.append(tempList)

#     if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
#         if blink == True:
#             blink = False
#         else: blink = True         
#     glutPostRedisplay()

# def keyboardListener(key, x, y):
#     global pause
#     if key==b' ':
#         if pause == True:
#             pause = False
#         else:
#             pause = True
#     glutPostRedisplay()

# def specialKeyListener(key, x, y):
#     global pause, speed, direction_color
#     if pause == False:
#         if key == GLUT_KEY_UP:
#             speed *= 1.5
#             for i in range(len(direction_color)):
#                 direction_color[i][0] = (min(direction_color[i][0][0] * 1.5, 4)), (min( direction_color[i][0][1] * 1.5, 4))
#         elif key == GLUT_KEY_DOWN:
#             speed /= 1.5
#             for i in range(len(direction_color)):
#                 direction_color[i][0] = (max(direction_color[i][0][0] / 1.5,0.2)),(max( direction_color[i][0][1] / 1.5,0.2))
#     glutPostRedisplay()

# def viewPoints():
#     global points, blink, direction_color, ball_size
#     for i in range(len(points)):
#         if i < len(direction_color):
#             glColor3f(direction_color[i][1][0], direction_color[i][1][1], direction_color[i][1][2])
#             if blink== True:
#                 glColor3f(0, 0, 0)
#             glPointSize(ball_size)
#             glBegin(GL_POINTS)
#             glVertex2f(points[i][0], points[i][1])
#             glEnd()
#             points[i] = (points[i][0] + direction_color[i][0][0], points[i][1] + direction_color[i][0][1])
#             if points[i][0] >= 299 or points[i][0] <= -299:
#                 direction_color[i][0] = (-direction_color[i][0][0], direction_color[i][0][1])
#             if points[i][1] >= 299 or points[i][1] <= -299:
#                 direction_color[i][0] = (direction_color[i][0][0], -direction_color[i][0][1])
    
#     blink = False

# def animation():
#     global pause
#     if pause == False:
#         glutPostRedisplay()


# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glClearColor(0, 0, 0, 0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     gluLookAt(0, 0, 300, 0, 0, 0, 0, 1, 0)
#     glMatrixMode(GL_MODELVIEW)
#     viewPoints()

#     glBegin(GL_LINES)
#     glColor3f(1, 1, 1)
#     glVertex2d(-300, -300)
#     glVertex2d(300, -300)
#     glVertex2d(300, -300)
#     glVertex2d(300, 300)
#     glVertex2d(300, 300)
#     glVertex2d(-300, 300)
#     glVertex2d(-300, 300)
#     glVertex2d(-300, -300)
#     glEnd()

#     glutSwapBuffers()

# def init():
#     glClearColor(0, 0, 0, 0)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(104, 1, 1, 1000)


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(Width, Height) 
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
# wind = glutCreateWindow(b"Ball movement") 
# init()
# glutDisplayFunc(showScreen)
# glutIdleFunc(animation)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)
# glutMainLoop()
