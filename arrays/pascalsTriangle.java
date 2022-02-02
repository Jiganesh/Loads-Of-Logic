package arrays;
import java.util.*;

// https://leetcode.com/problems/pascals-triangle/

public class pascalsTriangle{
    public static void main(String[] args) {
        SolutionPT solution = new SolutionPT ();

        print(solution.generate(6));
        print(solution.generate(0));
        print(solution.generate(1));
        print(solution.generate(20));


    }
    public static void print(List<List<Integer>> triangle){
        if (triangle.size()==0) System.out.println("No Element");
        for (List<Integer> i: triangle){
            System.out.println(i);
        }
        System.out.println();
    }
}

class SolutionPT{
    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();        
        if (numRows==0) return triangle ;
        
        List<Integer> firstrow = new ArrayList<Integer>();
        firstrow.add(1);
        triangle.add(firstrow);
        
        for(int i=1; i<numRows; i++){
            List<Integer> previousrow = triangle.get(i-1);
            List<Integer> currentrow = new ArrayList<Integer>();
            
            currentrow.add(1);
            for(int j=1; j<i; j++){
                int element = previousrow.get(j-1)+previousrow.get(j);
                currentrow.add(element);
            }
            currentrow.add(1);
            triangle.add(currentrow);
        }
        
        return triangle;
        
    }
}