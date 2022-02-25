// https://leetcode.com/problems/compare-version-numbers/
package strings;

public class compareVersionNumbers {
    public static void main(String[] args) {
        SolutionCVN solution = new SolutionCVN();
        System.out.println(solution.compareVersion("1.0.1", "1.0"));
        System.out.println(solution.compareVersion("1.0.1", "1.0.0"));
        System.out.println(solution.compareVersion("7.5.2.4", "7.5.3"));
    }
}


class SolutionCVN {

    // Submitted by @Jiganesh

    // TC : O(N)
    // SC : O(N)

    // Runtime: 1 ms, faster than 90.83% of Java online submissions for Compare Version Numbers.
    // Memory Usage: 42.5 MB, less than 8.43% of Java online submissions for Compare Version Numbers.
    
    public int compareVersion(String version1, String version2) {
        
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        
        for (int i =0 ; i< Math.max(v1.length, v2.length); i++){

            int val1 = (i<v1.length)?Integer.parseInt(v1[i]):0;
            int val2 = (i<v2.length)?Integer.parseInt(v2[i]):0;
            
            if (val1 < val2) return -1;
            else if(val1 > val2) return 1; 
        }
        return 0;
    }

     // Submitted by @Jiganesh

    // TC : O(N)
    // SC : O(1)

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for Compare Version Numbers.
    // Memory Usage: 42.6 MB, less than 6.00% of Java online submissions for Compare Version Numbers.
    
    public int compareVersionApproach2(String version1, String version2) {
        
        int i = 0, j = 0;

        while (i < version1.length() || j < version2.length()){

            int val1 = 0;
            while (i< version1.length() && version1.charAt(i) != '.') {
                val1 = val1*10 + version1.charAt(i++)-'0';
                
            }

            int val2 =0;
            while(j < version2.length() && version2.charAt(j) != '.'){
                val2 = val2*10 + version2.charAt(j++)-'0';
            }
            
            if (val1 < val2) return -1;
            else if (val1> val2) return 1;
            
            i++;
            j++;
            
        }
        return 0;
    }
}