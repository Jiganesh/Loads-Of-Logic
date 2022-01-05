package recursion;
import java.util.Arrays;

public class sumTriangleFromArray {
    public static void main(String[] args) {
        SolutionSTFA solution = new SolutionSTFA();
        solution.triangle(new int[] { 1, 2, 3, 4, 5 });
    }
}

class SolutionSTFA {

    public void triangle(int[] array) {
        
        if (array.length==0) return;
        int [] smallerArray = new int[array.length-1];
        for (int i=1; i< array.length;i++){
            smallerArray[i-1]= array[i-1]+array[i];
        }
        triangle(smallerArray);
        System.out.println(Arrays.toString(array));
    }

    // Checking if array if empty if it is then return ;
    // making smallerArray
    // calling funcion 
    // then printing

    /*
    triangle(3,5,7,9)
        -> triangle (8,12,16)
            -> triangle (20 ,28)
                -> triangle (48) 
                    -> triangle () return 
                -> print(48)
            -> print(20, 28)
        ->print(8,12,16)
    ->print(3,5,7,9)
->print(1,2,3,4,5)
    */
}