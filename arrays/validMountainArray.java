package arrays;

public class validMountainArray{
    public static void main(String[] args) {

        SolutionVMA solution = new SolutionVMA();
        System.out.println(solution.validMountainArrayMethod(new int[]{1,3,2}));
        System.out.println(solution.validMountainArrayMethodApproach2(new int[]{1,3,2}));

    }
}
class SolutionVMA {

    // Submitted by @kushvr

    public boolean validMountainArrayMethod(int[] arr) {
        
        int inc = 0;
        int dec = 0;
        int len = arr.length;
        int i = 0;
        int f = 0;
        
        if(len < 3 || arr[1] <= arr[0])
              return false;
        
        
        for( i=0;i<len - 1;i++){
  
            if(arr[i + 1] > arr[i]){
                if(f == 0){
                    inc++;
                    f = 1;
                }
            }else if(arr[i + 1] < arr[i]){
                if(f == 1){
                dec++;
                 f = 0;
                }
            }else if(arr[i + 1] == arr[i])
                      return false;
            
        }
        
        if(inc > 1 || dec > 1)
              return false;
        else if(inc == 1 && dec == 1)
               return true;
        
        return false;
    }

    
    // Submitted by @Jiganesh

    // TC : O(N)
    // SC : O(1)
    public boolean validMountainArrayMethodApproach2(int[] arr) {
        
        int i = 0;
        // reach the end of increasing order
        while (i< arr.length && i+1 <arr.length && arr[i]<arr[i+1]) i++;

        // check for edge case if no increasing order of all array is increasing order
        if (i==0 || i+1>=arr.length) return false;

        // after reaching end of increasing order return false if  next element is not smaller
        while(i<arr.length && i+1 < arr.length ) if (arr[i]<=arr[i++ +1]) return false;

        // if all array is traversed then return that it is valid
        return true;
        
    }
}
