package concepts.recursion;

import java.util.ArrayList; 

public class linearSearchWithDuplicateValuesInArray {
    public static void main(String[] args) {
        System.out.println(linearSearch(new int[]{10,1,10,10,3,7,2,8,9,10,5,6},10));
        System.out.println(linearSearch(new int[]{-0, 0,4,-1,-75,-2,2,63,0,0,22,21,43,11,25,0},0));
        System.out.println(linearSearch(new int[]{},10));

        System.out.println(searchWithCombiningResults(new int[]{10,1,10,10,3,7,2,8,9,10,5,6},10));
        System.out.println(searchWithCombiningResults(new int[]{-0, 0,4,-1,-75,-2,2,63,0,0,22,21,43,11,25,0},0));
        System.out.println(searchWithCombiningResults(new int[]{},10));
    }
    public static ArrayList<Integer> linearSearch(int[] array, int target){
        return helper (array, target,0, new ArrayList<Integer>());
    }
    public static ArrayList<Integer> helper(int[] array, int target , int index,ArrayList<Integer> list){
        if (index> array.length-1) return list;
        if ( array[ index]==target) list.add(index);
        return helper(array, target,index+1, list);
    }
    public static ArrayList<Integer> searchWithCombiningResults(int[] array ,int target){
        return helperII(array, target, 0);
    }

    public static ArrayList<Integer> helperII(int[] array, int target, int index){
        //Not good approach so don't use it because you are creating objects again and again
        ArrayList <Integer> list = new ArrayList<Integer>();
        if(index >array.length-1) return list;
        if(array[index]== target) list.add(index);
        
        ArrayList<Integer> findInRemainingList = helperII(array, target, index+1);
        list.addAll(findInRemainingList);
        return list;
    }
}
