def gestureforlondon4():
  neopixel.setAnimation("Color Wipe", 0, 20, 0, 1)
  sleep(2)
  neopixel.setAnimation("Ironman", 0, 0, 255, 1)
#welcome  
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(0,90,90,50,65)
  i01.moveHead(0,90)
  rollneck.moveTo(90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  sleep(5)
#welcome close hand
  i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,40)
  rollneck.moveTo(50)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)
#welcome close hand 2
  i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,120)
  rollneck.moveTo(120)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)
#welcome close hand3
  i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(0,40,25,40,65)
  i01.moveHead(0,90)
  rollneck.moveTo(90)
  i01.moveArm("left",26,105,30,25)
  i01.moveArm("right",37,124,30,27)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  sleep(3)  
#davinci  
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  rollneck.moveTo(50)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn wrist 1 
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  rollneck.moveTo(50)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,10)
  i01.moveTorso(95,90,90)
  sleep(1) 
#davinci turn wrist 2  
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",180,180,180,180,180,180)
  i01.moveTorso(95,90,90)
  sleep(2) 
#davinci turn wrist 3 
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,10)
  i01.moveTorso(95,90,90)
  sleep(1) 
#davinci  
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,10,42,50,65)
  i01.moveHead(46,10)
  rollneck.moveTo(90)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",61,49,14,38,15,64)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(1)
#davinci turn head close hand 1   
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  #i01.moveHead(46,160,130,40,65)
  i01.moveHead(46,160)
  rollneck.moveTo(120)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",180,180,180,180,180,10)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn head close hand 2   
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  i01.moveHead(46,160)
  #i01.moveHead(46,160,130,40,65)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",0,0,0,0,0,180)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)
#davinci turn head close hand 3   
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.90)
  #i01.moveHead(46,160,130,40,65)
  i01.moveHead(46,160)
  i01.moveArm("left",9,115,28,80)
  i01.moveArm("right",13,118,26,80)
  i01.moveHand("left",180,180,180,180,180,10)
  i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(95,90,90)
  sleep(2)         
#close hands and turn both wrist 
  #i01.moveHead(50,50,60,90,65)
  i01.moveHead(50,50)
  rollneck.moveTo(90)
  i01.moveArm("left",88,103,75,28)
  i01.moveArm("right",80,97,76,21)
  i01.moveHand("left",180,180,180,180,180,170)
  i01.moveHand("right",180,180,180,180,180,10)
  i01.moveTorso(90,90,90)   
  sleep(3)
#dab left  
  i01.setHandSpeed("left", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  #i01.moveHead(79,160,120,90,65)
  i01.moveHead(79,160)
  i01.moveArm("left",5,84,32,78)
  i01.moveArm("right",87,82,123,74)
  i01.moveHand("left",0,0,0,0,0,25)
  i01.moveHand("right",0,0,0,0,0,113)
  i01.moveTorso(170,120,90)
  sleep(6)
#arms up and centered  
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("left", 0.9,  0.9,  0.9,  0.9)
  i01.setArmSpeed("right",  0.9,  0.9,  0.9,  0.9)
  i01.setHeadSpeed(0.8, 0.8)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  #i01.moveHead(60,50,70,90,65)
  i01.moveHead(60,50)
  i01.moveArm("left",75,90,120,10)
  i01.moveArm("right",75,90,120,10)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",180,180,180,180,180,113)
  i01.moveTorso(90,90,90) 
  sleep(3)
#dab right
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("left", 0.9,  0.9,  0.9,  0.9)
  i01.setArmSpeed("right",  0.9,  0.9,  0.9,  0.9)
  i01.setHeadSpeed(0.8, 0.8)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)  
  i01.moveHead(60,20)
  i01.moveArm("left",87,90,123,74)
  i01.moveArm("right",5,84,32,80)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(40,70,90)
  sleep(6)
#welcome  
  i01.setHandSpeed("left", 0.80, 0.80, 0.80, 0.80, 0.80, 0.80)
  i01.setHandSpeed("right", 0.80, 0.80, 0.80, 0.80, 0.80, 0.80)
  i01.setArmSpeed("left", 0.80, 0.80, 0.80, 0.80)
  i01.setArmSpeed("right", 0.80, 0.80, 0.80, 0.80)
  i01.setHeadSpeed(0.90, 0.90)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)  
  #i01.moveHead(0,90,90,50,65)
  i01.moveHead(0,90)
  i01.moveArm("left",15,105,30,20)
  i01.moveArm("right",25,124,30,20)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(5)
