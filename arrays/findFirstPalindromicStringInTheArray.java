package arrays;

public class findFirstPalindromicStringInTheArray {
    public static void main(String[] args) {
        SolutionFFPSITA solution = new SolutionFFPSITA();
        System.out.println(solution.firstPalindrome(new String[]{"abc","car","ada","racecar","cool"})); //ada
    }
    
}

class SolutionFFPSITA {
    public String firstPalindrome(String[] words) {
        for (String word: words){
            if(checkPalindrome(word)) return word;
        }
        return "";
        
    }
    
    public boolean checkPalindrome(String word ){
        int start = 0;
        int end = word.length()-1;
        
        while(start<end){
            if( Character.compare(word.charAt(start), word.charAt(end)) !=0) return false;
            start++;
            end--;
        }
        return true;
    }
}