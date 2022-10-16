//Leetcode = https://leetcode.com/problems/last-stone-weight/
import java.util.*;

class lastStoneWeight
 {
    public int lastStoneWeight(int[] stones) {
        
        PriorityQueue<Integer> pq  = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i: stones){
            pq.add(i);
        }
        
        while(pq.size()>1){
            int y = pq.poll();
            int x = pq.poll();
            if(y != x){
                pq.add(y-x);
            }
        }
        return pq.size()==0?0:pq.poll();
    }
}