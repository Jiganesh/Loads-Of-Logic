public class FindTheSmallestLetterGreaterThanTarget {
    public static void main(String[] args) {
        char target = 'a';
        char[] letters = {'c', 'f', 'j'};
        char result = nextGreatestLetter(letters, target);
        System.out.println(result);
    }

    public static char nextGreatestLetter(char[] letters, char target) {
        int start = 0;
        int end = letters.length;
        
        while (start<= end){
            int mid = start +(end - start)/2;
            if (letters[mid] < target){
                start = mid +1;
            }else{
                end = mid-1 ;
            }
        }
        return letters[start+1];
    }
}
    

