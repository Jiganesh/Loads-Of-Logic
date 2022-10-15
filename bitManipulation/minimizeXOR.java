// https://leetcode.com/problems/minimize-xor
/*
Time complexity:O(n)
Space Complexity:O(1)
*/
class Solution {

    public int minimizeXor(int num1, int num2) {

        int cnt = Integer.bitCount(num2);
        cnt -= Integer.bitCount(num1);
        int curr = 1;
        while (cnt != 0){
            if (cnt < 0 && (num1 & curr) != 0){  
                num1 ^= curr;
                cnt++;
            } 
            else if (cnt > 0 && (num1 & curr) == 0){ 
                num1 |= curr; 
                cnt--;
            }

            curr <<= 1;
        }

        return num1;
    }
}
