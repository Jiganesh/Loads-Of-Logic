package strings;

public class stringToInteger{
    public static void main(String[] args) {
        SolutionSTI solution = new SolutionSTI();
        System.out.println(solution.myAtoi("        -42"));
        System.out.println(solution.myAtoi("457 with words"));
        System.out.println(solution.myAtoi("with words 987"));
        System.out.println(solution.myAtoi("2147483646"));
        System.out.println(solution.myAtoi("-+12"));
        System.out.println(solution.myAtoi("9223372036854775808"));
        System.out.println(solution.myAtoi("-314159265359"));

    }
}

class SolutionSTI {

    // TC = O(N)
    // SC = O(1)
    public int myAtoi(String s) {

        // Thing we need to do 
        // i . Ignore leading spaces

        // ii. Check if the next character (if not already at the end of the string) is '-' or '+'. 
        // Read this character in if it is either + - to determine final ans
        // Assume the result is positive if neither is present
        // if we encounter -+12 we should give 0 because we can only treat - as sign 

        // iii. if we encounter any character which is not valid num remaining string is invalid

        // iV.  if value in not in range of Integer we return limits according the value
        
        
        int res =0;
        int negative =1;
        int pointerAtChar = 0;
        int lengthOfString = s.length();

        // Neglecting leading spaces
        while(pointerAtChar< lengthOfString && s.charAt(pointerAtChar)==' ') pointerAtChar++;

        // checking if there is any sign or not
        if (pointerAtChar< lengthOfString && s.charAt(pointerAtChar)=='-'){
            pointerAtChar++;
            negative= -1;
        }else if (pointerAtChar< lengthOfString && s.charAt(pointerAtChar)=='+'){
            pointerAtChar++;
            negative =1; 
        }

        while(pointerAtChar< lengthOfString && s.charAt(pointerAtChar)>='0' && s.charAt(pointerAtChar)<='9'){
            int digit = s.charAt(pointerAtChar)-'0';
            if (res< Integer.MAX_VALUE/10 || (res == Integer.MAX_VALUE/10 &&  digit <= Integer.MAX_VALUE%10)){
                res = res*10+digit;
            }else{
                return (negative==-1)? Integer.MIN_VALUE: Integer.MAX_VALUE;
            }
            pointerAtChar++;
            
        }
        return res*negative;
    }
}
