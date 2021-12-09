package binarySearch;
// Solution to this problem is given using HashMap
import java.util.HashMap;

public class checkIfNAndItsDoubleExist {
    public static void main(String[] args) {
        SolutionCINAIDE solution = new SolutionCINAIDE();
        System.out.println(solution.checkIfExist(new int[] {10,2,5,3})); //true
        System.out.println(solution.checkIfExist(new int[] {7,1,14,11})); //true
        System.out.println(solution.checkIfExist(new int[] {3,1,7,11})); //false
    }
}

class SolutionCINAIDE  {

    // Solved With HashMap Approach
    public boolean checkIfExist(int[] arr) {
        
        HashMap<Integer, Integer> dictionary = new HashMap<Integer,Integer>();
        for (int i : arr){
            if ((i%2==0 && dictionary.containsKey(i/2)) || dictionary.containsKey(i*2)) return true;
            dictionary.put(i,i*2);
        }
        return false;
    }
}
