package recursion;

public class numberOfStepsToReduceANumberToZero {
    public static void main(String[] args) {
        SolutionNOSTRANTZ solution = new SolutionNOSTRANTZ();
        System.out.println(solution.numberOfSteps(14));
        System.out.println(solution.numberOfSteps(123));
    }
    
}

class SolutionNOSTRANTZ {
    public int numberOfSteps(int num) {
        return helper(num, 0);
    }
    public int helper (int num , int count){
        if (num==0) return count;
        if ((num &1 )==1) return helper(num-1, count+1);
        else  return helper (num/2 , count+1);
    }
}