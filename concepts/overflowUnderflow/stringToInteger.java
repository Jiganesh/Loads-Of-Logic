package concepts.overflowUnderflow;

public class stringToInteger {
    public static void main(String[] args) {
        System.out.println(validInteger("-2147483648"));
        System.out.println(validInteger("-2147483649"));
        System.out.println(validInteger("2147483648"));
        System.out.println(validInteger("2147483647"));
    }

    public static int validInteger(String s){
        int res =0, pointerAtChar =0; 
        int negative=1;
        int lengthOfString = s.length();
        
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
