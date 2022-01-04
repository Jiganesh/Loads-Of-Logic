package arrays;

public class sortColors {
    public static void main(String[] args) {

        SolutionSC solution = new SolutionSC();
        int[] array=new int[]{2,0,2,1,1,0};
        solution.sortColorsApproach2(array);
        print(array);
    }

    public static void print(int[]array){
        for (int i: array) System.out.print(i+" ");
        System.out.println();
    }
}


class SolutionSC {

    //Insertion Sort
    public void sortColors(int [] array){

        for(int i =0 ; i<array.length; i++){
            int key =array[i];
            int j = i-1;
            while (j>=0 && array[j]>key){
                array[j+1]= array[j];
                j--;
            }
            array[j+1]=key;
        }
    }

    //Counting Sort

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Sort Colors.
    // Memory Usage: 39 MB, less than 19.26% of Java online submissions for Sort Colors.

    public void sortColorsApproach2(int [] array){
        int red=0 , white=0 , blue =0;
        for (int i=0 ; i< array.length; i++){
            switch(array[i]){
                case 0:
                    red++;
                    break;
                case 1:
                    white++;
                    break;
                case 2:
                    blue++;
                    break;
            }
        }
        int i =0;
        while (red>0 || white >0 || blue >0){
            if (red >0) {array[i]=0; red--;}
            else if (white >0) {array[i]=1;white--;}
            else if (blue >0) {array[i]=2; blue--;}
            i++;
        }
    }
    

    //Swapper 
    //One Pass In place solution
    public void sortColorsApproach3(int [] array){
        int low=0, mid = 0;
        int high=array.length-1;

        while (mid<=high ){
            if (array[mid]==0){
                swap(array, low, mid);
                low++;
                mid++;
            }else if (array[mid]==1){
                mid++;
            }else if (array[mid]==2) {
                swap(array, mid, high);
                high--;
            }
        }   
    }
    
    public static void swap (int [] array , int i, int j){
        int temp =  array[i];
        array[i] = array[j];
        array[j] = temp;
    }



}