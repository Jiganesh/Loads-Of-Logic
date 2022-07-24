package binarySearch;

public class sqrtx {
    public static void main(String[] args) {
        SolutionSqrtx solution = new SolutionSqrtx();
        System.out.println(solution.mySqrt(4));
        System.out.println(solution.mySqrt(190));
        System.out.println(solution.mySqrt(16));
        System.out.println(solution.mySqrt(14));

    }
    
}

class SolutionSqrtx {
    public int mySqrt(int x) {
        
        long start =0;
        long end = x;
        while (start <= end){
            long mid = start+ (end -start)/2;
            long sqr = mid*mid;
            if (sqr > x) end = mid-1;
            else if(sqr<x) start =mid+1;
            else return (int) mid;
        }
        return (int)end;
    }
}