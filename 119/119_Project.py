#import turtle and define player
import turtle as trtl
player=trtl.Turtle()
player.shape("turtle")

#define wn
wn=trtl.Screen()

#input maze level and define start, correct movements and amount of movement
mapchosen = 0
while (mapchosen==0):
  map=int(input("Choose level 1, 2, or 3: "))
  if (map ==1):
    wn.bgpic("Level1.png")
    startx=-190
    starty=-190
    def move():
      player.fd(190)
    correct_moves=["f", "f", "r","r","l","l"]
    mapchosen=1
  elif(map ==2):
    wn.bgpic("Level2.png")
    startx=-217
    starty=-217
    endx = 218
    endy = 218
    def move():
      player.fd(145)
    correct_moves = ["r", "l", "l", "r", "r", "f", "r", "f", "l", "l", "f", "f"]
    mapchosen=1
  elif (map==3):
    wn.bgpic("Level3.png")  
    startx=-248
    starty=-230
    endx = 192
    endy = 210
    def move():
      player.fd(110)
    correct_moves = ["f", "f", "r", "r", "f", "l", "l", "f", "f", "f", "r", "f"]
    mapchosen=1
  elif (map>3):
    print("Invalid map number!")
  elif (map<1):
    print("Invalid map number!")

#go to start
gaming = 1
player.penup()
player.goto(startx, starty)
player.setheading(90)
player.pendown()
attempt = 1
print ("Attempt 1")

#The player moves
while (gaming == 1):
  for walk in correct_moves:
    step=input("Where do you want to go next? Forward (f), Left (l), or Right (r)?")
    if (step == "r"):
      player.right(90)
    if (step=="l"):
      player.left(90)
    move()
    playerx = player.xcor()
    playery = player.ycor()
    #restart from beginning
    if (step != walk):
      attempt += 1
      player.fillcolor("red")
      player.dot(15)
      correct_moves.clear()
      if (map == 1):
        correct_moves=["f", "f", "r","r","l","l"]
      elif (map == 2):
        correct_moves = ["r", "l", "l", "r", "r", "f", "r", "f", "l", "l", "f", "f"]
      elif (map == 3):
        correct_moves = ["f", "f", "r", "r", "f", "l", "l", "f", "f", "f", "r", "f"]
      player.penup()
      player.goto(startx,starty)
      player.setheading(90)
      player.pendown()
      player.fillcolor("black")
      print("Attempt", attempt)
    #victory scenario
    if (playerx >= endx):
      if (playery >= endy):
        player.fillcolor("green")
        gaming=0


#end player movement 
wn.mainloop()
