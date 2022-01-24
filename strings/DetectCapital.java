class Solution {
    public boolean detectCapitalUse(String word) {
        
        int len = word.length();
        int caps = 0;
        int fst_cap = 0;
        
        for(int i=0;i<len;i++){
            int k = (int)(word.charAt(i));
            if(k>= 65 && k<= 90){
                caps++;
                if(i == 0)
                    fst_cap = 1;
            } 
        }
        
        
        if(caps == 0)
              return true;
        else if(fst_cap == 1 && caps == 1)
               return true;
        else if(caps == len)
              return true;
        else
              return false;
        
        
    }
}
