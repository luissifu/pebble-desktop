import math
from socket import *
from pymouse import PyMouse

mouse = PyMouse()
x_dim, y_dim = mouse.screen_size()
x = x_dim / 2
y = y_dim / 2

mouse.move(x,y)

UDP_IP = "10.12.173.15"
UDP_PORT = 12345

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024)
  
  parts = data.split(',')
  
  nx = float(parts[0]) * 10
  ny = float(parts[1]) * 10

  x = x + int(nx)
  y = y + int(ny)

  if x < 0:
    x = 0
  elif x > x_dim:
    x = x_dim

  if y < 0:
    y = 0
  elif y > y_dim:
    y = y_dim

  mouse.move(x,y)

  print "x: %d, y: %d" % (x, y)
  print "received message:", data