My first impulse was to use a stack and then evaluate that stack to see if the robot returned to the origin. However, I realized that
I could easily just track the X and Y position of the bot as I evaluated the string that represented the bots movement. Then at the end
of the movement I could just make sure the position was (0,0)