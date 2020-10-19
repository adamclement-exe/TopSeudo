import time 

SET answer_A TO ["A", "a"]
SET answer_B TO ["B", "b"]
SET answer_C TO ["C", "c"]
SET yes TO ["Y", "y", "yes"]
SET no TO ["N", "n", "no"]

SET sword TO 0
SET flower TO 0
SET required TO ("\nUse only A, B, OR C\n") 

PROCEDURE intro():
BEGIN PROCEDURE
  SEND ("After a drunken night out with friends, you awaken the "
  "next morning in a thick, dank forest. Head spinning AND " 
  "fighting the urge to vomit, you stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "grotesque sound emitting behind you. A slobbering orc is "
  "running towards you. You will:") TO SCREEN
  time.sleep(1)
  SEND ("""  A. Grab a nearby rock and throw it at the orc
  B. Lie down AND wait to be mauled
  C. Run""") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in answer_A THEN
    option_rock()
  ELSEIF choice in answer_B THEN
    SEND ("\nWelp, that was quick. "
    "\n\nYou died!") TO SCREEN
  ELSEIF choice in answer_C THEN
    option_run()
  ELSE
    SEND (required) TO SCREEN
    intro()
PROCEDURE option_rock(): 
BEGIN PROCEDURE
  SEND ("\nThe orc is stunned, but regains control. He begins "
  "running towards you again. Will you:") TO SCREEN
  time.sleep(1)
  SEND ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in answer_A THEN
    option_run()
  ELSEIF choice in answer_B THEN
    SEND ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "orc's head. You missed. \n\nYou died!") TO SCREEN
  ELSEIF choice in answer_C THEN
    option_cave()
  ELSE
    SEND (required) TO SCREEN
    option_rock()
PROCEDURE option_cave():
BEGIN PROCEDURE
  SEND ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in yes THEN
    SET sword TO 1 
  ELSE
    SET sword TO 0
  SEND ("\nWhat do you do next?") TO SCREEN
  time.sleep(1)
  SEND ("""  A. Hide in silence
  B. Fight
  C. Run""") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in answer_A THEN
    SEND ("\nReally? You're going to hide in the dark? I think "
    "orcs can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!") TO SCREEN
  ELSEIF choice in answer_B THEN
   IF sword > 0 THEN
    SEND ("\nYou laid in wait. The shimmering sword attracted "
    "the orc, which thought you were no match. As he walked "
    "closer AND closer, your heart beat rapidly. As the orc "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!") TO SCREEN
   ELSE: 
     SEND ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!") TO SCREEN
  ELSEIF choice in answer_C THEN
    SEND ("As the orc enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around AND sees you running.") TO SCREEN
    option_run()
  ELSE
    SEND (required) TO SCREEN
    option_cave()
PROCEDURE option_run():
BEGIN PROCEDURE
  SEND ("\nYou run as quickly as possible, but the orc's "
  "speed is too great. You will:") TO SCREEN
  time.sleep(1)
  SEND ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in answer_A THEN
    SEND ("You're easily spotted. "
    "\n\nYou died!") TO SCREEN
  ELSEIF choice in answer_B THEN
    SEND ("\nYou're no match FOR an orc. "
    "\n\nYou died!") TO SCREEN
  ELSEIF choice in answer_C THEN
    option_town()
  ELSE
    SEND (required) TO SCREEN
    option_run()
PROCEDURE option_town():
BEGIN PROCEDURE
  SEND ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down AND grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N") TO SCREEN
  SET choice TO RECIEVE (">>>") FROM KEYBOARD
  IF choice in yes THEN
    SET flower TO 1 
  ELSE
    SET flower TO 0
  SEND ("You hear its heavy footsteps and ready yourself FOR "
  "the impending orc.") TO SCREEN
  time.sleep(1)
  IF flower > 0 THEN
    SEND ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "FOR love. "
    "\n\nThis got weird, but you survived!") TO SCREEN
  ELSE: 
     SEND ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!") TO SCREEN
intro()
