package concepts.recursion;

public class linearSearchUsingRecursion {
    public static void main(String[] args) {
        System.out.println(linearSearch(new int[]{1,3,7,2,8,9,10,5,6},10));
        System.out.println(linearSearch(new int[]{-4,-1,-75,-2,2,63,22,21,43,11,25,0},0));
        System.out.println(linearSearch(new int[]{},10));
    }

    public static int linearSearch(int[] array, int target){
        return helper(array , target,0);
    }
    public static int helper(int[] array , int target, int index){
        if (index > array.length-1) return -1;
        else if (array[index]== target) return index;
        return helper(array, target,index+1);
    }
}
