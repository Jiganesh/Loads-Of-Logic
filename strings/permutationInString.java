package strings;

// https://leetcode.com/problems/permutation-in-string/

public class permutationInString{
    public static void main(String[] args) {
        SolutionPIS solution = new SolutionPIS();
        System.out.println(solution.checkInclusion("ab", "eidbaooo"));
    }
}
class SolutionPIS {
    
    public boolean check(int[] a, int[] b){
        for(int i=0;i<26;i++){
            if(a[i] != b[i])
                return false;
        }
        return true;
            
    }
    
    public boolean checkInclusion(String s1, String s2) {
        
        int l1 = s1.length();
        int c1[] = new int[26];
        for(int i=0;i<l1;i++)
            c1[(int)s1.charAt(i) - 97]++;
        
        
        int l2 = s2.length();
        if(l2 < l1){
            return false;
        }else{
            int c2[] = new int[26];
           
            for(int i=0;i<l1;i++)
                c2[(int)s2.charAt(i) - 97]++;
            
            if(check(c1,c2))
                return true;
            else{
                
                for(int i=l1;i<l2;i++){
                    int k = (int)s2.charAt(i) - 97;
                    int tar = (int)s2.charAt(i - l1) - 97;
                    c2[k]++;
                    c2[tar]--;
                    if(check(c1,c2))
                         return true;
                }
                return false;
            }
            
       }      
        
    }
}
