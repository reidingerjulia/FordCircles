import farey
import pyglet
from pyglet import shapes
import random
import itertools

f = farey.Farey(5)


window = pyglet.window.Window(1000, 1000) # 1000 = 1
batch = pyglet.graphics.Batch()



def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

circles = []
def renderFordCircles():
    # need to be in memory in order to be drawn
    for (r, elems) in f.seq:
        # calc color
        rgb = random_color_generator()

        for ele in elems:
            x = ele[0]/ele[1]
            y = 1/(2*ele[1]*ele[1])
            r = 1/(2*ele[1]*ele[1])
            circles.append(shapes.Circle(x*1000, y*1000, r*1000, color=rgb, batch=batch))

renderFordCircles()

@window.event
def on_mouse_press(x, y, button, modifiers):
    renderFordCircles()

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()