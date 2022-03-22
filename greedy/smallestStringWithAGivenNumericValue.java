// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/


package greedy;

public class smallestStringWithAGivenNumericValue {
    public String getSmallestString(int n, int k) {
       StringBuilder sb=new StringBuilder("");

        for(int i=1;i<n + 1;i++){
             sb.append("a");
            k--;
        }
 
        int len = n - 1 ;
        while(true){
            if(k == 0)
                break;
        if(k > 0){
            k++;
            if(k <= 26 && k >= 1){
               sb.replace(len,len + 1,(char)(96 + k)+"" );
               k = 0;
            }else{
                sb.replace(len,len + 1,(char)(96 + 26)+"");
                k = k - 26;
            }
            len--;
        }
        }
  
         String answer = sb +"";
        return answer;
    }
}
