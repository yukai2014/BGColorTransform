# -*- coding:utf-8- -*-
from PIL import Image
from PIL import ImageFilter

def ChangePicBackground(img, from_color, to_color):
  if img is None:
    return
  if not set([from_color,to_color]).issubset(set(["r", "g", "b", "w"])):
      print "invalid color"
      return
  new_color = {'r': (255,0,0),
               'g': (0,255,0),
               'b': (0,0,255),
               'w': (255,255,255)
               }
  for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
      r,g,b = img.getpixel((x,y))
      bands = [r, g, b]
      if ( from_color in ('r','g','b')):
        original = bands.pop(('r','g','b').index(from_color))
        if original-bands[0] >= 30 and original - bands[1] >= 30:
          img.putpixel((x,y), new_color[to_color])
      elif from_color == 'w':
        if ( r >= 200 and g >= 200 and b >= 200):
          img.putpixel((x,y), new_color[to_color])

def PrintX():
  print 1212
