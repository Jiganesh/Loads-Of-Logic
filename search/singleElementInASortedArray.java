package search;

public class singleElementInASortedArray {
    public static void main(String[] args) {
        SolutionSEIASA solution = new SolutionSEIASA();
        System.out.println(solution.singleNonDuplicate(new int[] {1,1,2,3,3,4,4,8,8}));
        System.out.println(solution.singleNonDuplicate(new int[] {1,2,2,3,3,4,4}));
        System.out.println(solution.singleNonDuplicate(new int[] {2,2,3,3,4,4,5}));
    }
}

class SolutionSEIASA {
    public int singleNonDuplicate(int[] array) {

        int start = 0 ;
        int end  = array.length-1;

       while(start<end){
           int mid = start + (end -start)/2;

           if(array[mid]== array[mid+1]) mid = mid-1 ;
           if((mid -start+1 )%2 != 0) end = mid;
           else start = mid+1;
       }
       return array[start];   
    }
}