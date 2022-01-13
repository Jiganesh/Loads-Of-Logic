// https://leetcode.com/problems/robot-bounded-in-circle/

// Solution From : https://www.youtube.com/watch?v=nKv2LnC_g6E&t=534s

package strings;

public class robotBoundedInCircle{
    public static void main(String[] args) {
        SolutionRBC solution = new SolutionRBC();
        System.out.println(solution.isRobotBounded("LLGRL"));
        System.out.println(solution.isRobotBounded("LLGGLL"));
        System.out.println(solution.isRobotBounded("GGLR"));
        System.out.println(solution.isRobotBounded("GGLLGG"));
    }
}
class SolutionRBC {

    //TC : O(N)
    //SC : O(1)
    public boolean isRobotBounded(String instructions) {

        int dirX=0, dirY =1 ,x=0 ,  y=0;
        
        for (int i =0 ; i< instructions.length();i++){
            if (instructions.charAt(i)=='G'){
                x=x+dirX;
                y = y+dirY;
            }else if (instructions.charAt(i)=='L'){
                // Geometry
                int temp = dirX;
                dirX= -1*dirY;
                dirY= temp;  
            }else if(instructions.charAt(i)=='R'){
                // Geometry
                int temp = dirX;
                dirX= dirY;
                dirY= -1*temp;
                
            }           
        }
        // at last the robot should not be at initial position
        // the robot should face any other direction for cicle or loop to exist
        return (x==0 && y==0 )|| !(dirX ==0 && dirY==1) ;
    }
}