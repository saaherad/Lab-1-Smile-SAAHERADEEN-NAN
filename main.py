from browser import document, html, window, alert
import random 
def sketch (p):# this p is needed. 
  # it will be the proccessing sketch itself. to do things like background color. background(0) instead of p.background(0)
  
  def setup():
    p.createCanvas(700,410)
    p.background(255)
    p.rectMode(p.CENTER)
    
  def draw():
    colorList= ["lavender", "pink", "cyan", "red", ""]
    p.noStroke()
    p.fill(random.choice(colorList))
    p.ellipse(p.mouseX, p.mouseY,50,50)
    
  def mousePressed(self):
    p.background(0)
    
  def keyPressed(self):
    if p.key == " ":
      print("ALOHA!!")
      
  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed

myp5 = window.p5.new(sketch)