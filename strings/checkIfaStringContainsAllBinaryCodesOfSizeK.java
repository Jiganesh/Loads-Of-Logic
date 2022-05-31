package string;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

public class checkIfaStringContainsAllBinaryCodesOfSizeK {
    public static boolean hasAllCodes(String s, int k) {
        int count = 1 << k; // this is same as 2^K
        Set<String> res = new HashSet<>();
        for (int i = k; i <= s.length(); i++) {
            String temp = s.substring(i - k, i);
            if (!res.contains(temp)) {
                res.add(temp);
                count--;
            }
            if (count == 0)
                return true;
        }
        return false;
    }
}
