package arrays;

public class findTheHighestAltitude {
    public static void main(String[] args) {
        SolutionFTHA solution = new SolutionFTHA();

        System.out.println(solution.largestAltitude(new int[]{-5,1,5,0,-7}));
        System.out.println(solution.largestAltitude(new int[]{-4,-3,-2,-1,4,3,2}));

    }
    
}

class SolutionFTHA {
    public int largestAltitude(int[] gain) {
        
        int sum =0;
        int max = 0;
        
        for (int i: gain){
            sum+=i;
            max = (max >sum)?max: sum;
        }
        return max;
        
    }
}
