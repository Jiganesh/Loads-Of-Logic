package arrays;

public class findNumbersWithEvenNumbersOfDigits {
    public static void main(String[] args) {
        SolutionFNWENOD solution = new SolutionFNWENOD();
        System.out.println(solution.findNumbers(new int[]{12,345,2,6,7896}));
        System.out.println(solution.findNumbers(new int[]{555,901,482,1771}));
        System.out.println(solution.findNumbersApproach2(new int[]{12,345,2,6,7896}));
        System.out.println(solution.findNumbersApproach2(new int[]{555,901,482,1771}));


    }
    
}

class SolutionFNWENOD {

    //TC : O(N^2)
    //SC : O(1)
    public int findNumbers(int[] nums){
        int count = 0 ;
        for (int i =0 ; i< nums.length; i++){
            count += lengthOfNumberEvenOrNot(nums[i]);
        }
        return count;
    }
    public int lengthOfNumberEvenOrNot(int num){
        // if length of number is even then this function return 1 (true) else 0;
        int count =0;
        while(num>0){
            count++;
            num/=10;
        }
        return (count%2==0)? 1: 0;
    }

    //TC : O(N);
    //SC : O(1)
    public int findNumbersApproach2(int[] nums) {  
        int count =0;
        for (int num : nums)if (((int) Math.log10(num)+1)%2==0) count++;
        return count;  
    }
}