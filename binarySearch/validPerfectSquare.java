package binarySearch;

public class validPerfectSquare {
    public static void main(String[] args) {
        SolutionIPS solution = new SolutionIPS();
        System.out.println(solution.isPerfectSquare(16));
        System.out.println(solution.isPerfectSquare(14));
    }
    
}

class SolutionIPS {
    public boolean isPerfectSquare(int num) {
        long start = 0;
        long end = num;
        
        while(start <= end ){
            long mid = start + (end - start)/2;
            long sqr = mid * mid;
            if(sqr < num) start = mid +1;
            else if (sqr > num) end = mid-1;
            else return true;
        }
        return (int)(end)*(int)(end)==num;
    }
}