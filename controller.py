from pymouse import PyMouse

mouse = PyMouse()
x_dim, y_dim = mouse.screen_size()
x = x_dim / 2
y = y_dim / 2

mouse.move(x,y)
