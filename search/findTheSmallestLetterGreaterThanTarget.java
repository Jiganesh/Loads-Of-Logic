// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

package search;
public class findTheSmallestLetterGreaterThanTarget {
    public static void main(String[] args) {
        char target = 'c';
        char[] letters = {'a', 'b', 'c', 'd', 'f'};
        SolutionFTSLGTT solution = new SolutionFTSLGTT();
        char result = solution.nextGreatestLetter(letters, target);
        System.out.println(result);       
    }
}

class SolutionFTSLGTT{
    public char nextGreatestLetter(char[] array, char target) {
        int start =0;
        int end =array.length-1;


        while (start<= end){
            int mid = start + (end-start)/2;
            if(array[mid]<=target){
                start = mid+1;
            }else {
                end = mid-1;
            }
        }

        return array[start%array.length];
    }
}
