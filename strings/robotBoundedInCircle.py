class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        dirX , dirY = 0,1
        x, y = 0,0
        
        for i in instructions:
            if i == "G": 
                x,y=x+dirX,y+dirY
            elif i =="L":
                dirX,dirY = -1*dirY,dirX
            elif i =="R":
                dirX,dirY = dirY, -1*dirX
                
        # at last the robot should not be at initial position
        # the robot should face any other direction for cicle or loop to exist
        return (x,y)==(0,0) or (dirX,dirY)!=(0,1)
        