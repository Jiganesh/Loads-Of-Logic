// https://leetcode.com/problems/excel-sheet-column-number/

package strings;

public class excelSheetColumnNumber{
    public static void main(String[] args) {
        SolutionESCN solution = new SolutionESCN();
        System.out.println(solution.titleToNumber("A")); //1
        System.out.println(solution.titleToNumber("AB")); //28
        System.out.println(solution.titleToNumber("ZY")); //701
        System.out.println(solution.titleToNumber("FXSHRXW")); // 2147483647
        
    }
}


class SolutionESCN{

    // Submitted by @Jiganesh

    // TC : O(n)
    // SC : O(1)

    // Runtime: 1 ms, faster than 99.69% of Java online submissions for Excel Sheet Column Number.
    // Memory Usage: 41 MB, less than 37.91% of Java online submissions for Excel Sheet Column Number.
    
    public int titleToNumber(String columnTitle) {
        
        int result =0;
        int n = columnTitle.length()-1;
        
        for (int i=n ; i>=0; i--){
            result+=(columnTitle.charAt(n-i)-'A'+1)*Math.pow(26,i);
        }
        
        return result;
        
    }
}
