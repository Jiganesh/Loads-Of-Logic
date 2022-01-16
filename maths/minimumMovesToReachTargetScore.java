package maths;

public class minimumMovesToReachTargetScore {
    public static void main(String[] args) {
        SolutionMMTRTS solution = new SolutionMMTRTS();
        System.out.println(solution.minMoves(5, 0)); //4
        System.out.println(solution.minMoves(19, 2)); //7
        System.out.println(solution.minMoves(10, 5));//4 
        System.out.println(solution.minMoves(656101987, 1)); //328050994


        System.out.println(solution.minMovesApproach2(5, 0)); //4
        System.out.println(solution.minMovesApproach2(19, 2)); //7
        System.out.println(solution.minMovesApproach2(10, 5));//4 
        System.out.println(solution.minMovesApproach2(656101987, 1)); //328050994
        
    }
}

class SolutionMMTRTS {

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Minimum Moves to Reach Target Score.
    // Memory Usage: 37.9 MB, less than 20.00% of Java online submissions for Minimum Moves to Reach Target Score.
    

    // SIMPLE VERSION
    //TC : O(N) where N in MaxDoubles
    //SC : O(1)
    public int minMoves(int target, int maxDoubles) {

        int count =0;

        while (target >1 && maxDoubles > 0){
            if (target%2==0 && target/2>=1 && maxDoubles>=0) {
                maxDoubles--;
                target/=2;

            } else {
                target-=1;
            }

            count++;
        }
        return count+target-1;       
    }


    //TC : O(N) where N in MaxDoubles
    //SC : O(1)
    public int minMovesApproach2(int target, int maxDoubles) {

        int count =0;

        while (target >1 && maxDoubles--> 0){
            count += 1+ target%2;
            target/=2;
        }

        return count+target-1;       
    }
}
