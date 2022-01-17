class Solution {
    public boolean wordPattern(String pattern, String s) {
        
        
        HashMap<Character, String> al = new HashMap<Character, String>();
        String[] rs = s.split(" ");
        char[] ch = pattern.toCharArray();        
        HashSet<String> set = new HashSet<String>();
        int ch_len = ch.length;
        int rs_len = rs.length;
        
        if(ch_len != rs_len)
             return false;
        
        for(int i=0;i<ch_len;i++){
            if(al.get(ch[i]) == null){
                if(set.contains(rs[i]))
                      return false;
                al.put(ch[i],rs[i]);
                set.add(rs[i]);
            }
            else if(al.get(ch[i]).equals(rs[i]) == false){
                return false;
            }
 
        }
        
        return true;
        
        
    }
}
