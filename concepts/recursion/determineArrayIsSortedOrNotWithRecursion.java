package concepts.recursion;

public class determineArrayIsSortedOrNotWithRecursion{
    public static void main(String[] args) {
        System.out.println(sortedOrNot(new int []{1,4,5,8,9,10}));
        System.out.println(sortedOrNot(new int[] {1}));
        System.out.println(sortedOrNot(new int[] {-12 ,-4,0,4,1,2,3,9}));
    }
    public static boolean sortedOrNot(int[] array){
        return helper (array, 0);
    }
    public static boolean helper(int[] array, int index){
        if (index == array.length-1) return true ;
        return array[index] <= array[index+1] && helper(array, index+1);
    }
}