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
}