class Pair{
    int x;
    int y;
    Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}


class Solution {
    public List<Integer> partitionLabels(String s) {
        
        HashMap<Character, Integer> al = new HashMap<Character, Integer>();
        int len = s.length();
        for(int i=0;i<len;i++)
            al.put(s.charAt(i),i);
        
        ArrayList<Pair> part = new ArrayList<Pair>();
        
        int ind = 0;
        while(true){
            if(ind >= len)
                break;
            int a = al.get(s.charAt(ind));
             if(a > ind){
                 for(int i= ind + 1;i<a;i++){
                     if(al.get(s.charAt(i)) > a)
                         a  = al.get(s.charAt(i));
                 }
             }
            part.add(new Pair(ind, a));
            ind = a + 1;  
        }
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for(int i=0;i<part.size();i++)
          ans.add(part.get(i).y - part.get(i).x + 1);
       return ans; 
    }
}
