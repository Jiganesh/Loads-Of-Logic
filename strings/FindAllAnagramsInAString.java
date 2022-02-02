class Solution {
    
    public boolean Check(HashMap<Character, Integer> c1 , HashMap<Character, Integer> c2){
        
       for (Map.Entry<Character,Integer> entry : c2.entrySet())
       {
           char var = entry.getKey();
           if( c1.get(var) == null)
                 return false;
           int count = c1.get(entry.getKey());
           if(count != entry.getValue())
                return false;
                
       }
        
        return true;
        
    }
    
    public List<Integer> findAnagrams(String s, String p) {
        
        List<Integer> res = new ArrayList<Integer>();
        HashMap<Character, Integer> mp1 = new HashMap<Character, Integer>();
        
        int p_len = p.length();
        int s_len = s.length();

  for(int i=0;i<p_len;i++){
      if(mp1.get(p.charAt(i)) == null)
          mp1.put(p.charAt(i),1);
      else
          mp1.put(p.charAt(i), mp1.get(p.charAt(i)) + 1);
  } 
        
        if(p_len > s_len)
            return new ArrayList<Integer>();
        
        HashMap<Character, Integer> req = new HashMap<Character, Integer>();
     for(int i=0;i<p_len;i++){
         if(req.get(s.charAt(i)) == null)
          req.put(s.charAt(i),1);
      else
          req.put(s.charAt(i), req.get(s.charAt(i)) + 1);
     }
        
        List<Integer> result = new ArrayList<Integer>();
        
        boolean ck = Check(mp1,req);
        if(ck)
          result.add(0);
        int ind = 0;
            for(int i = p_len;i<s_len;i++){
                 if(req.get(s.charAt(ind)) == 1)
                      req.remove(s.charAt(ind));
                 else
                req.put(s.charAt(ind), req.get(s.charAt(ind)) - 1);
                
               if(req.get(s.charAt(i)) == null)
                   req.put(s.charAt(i), 1);
                else
                    req.put(s.charAt(i), req.get(s.charAt(i)) + 1);
                    
                boolean chk = Check(mp1,req);
                if(chk)
                    result.add(ind + 1);
                
                System.out.println("map   "+req+"    chk   "+chk+"  ss   "+i+"  ind  "+ind);
            ind++;
            }
         
        return result;            
           
   }}
