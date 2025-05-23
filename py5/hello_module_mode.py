



import py5

# do not: import * from py5
# https://py5coding.org/content/py5_modes.html


def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
