package arrays;

import java.util.HashSet;

public class checkIfTheSentenceIsPangram {
    public static void main(String[] args) {
        SolutionCITSIP solution = new SolutionCITSIP();
        System.out.println(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"));
    }

    
}

class SolutionCITSIP {


    // TC : O(N);
    // SC : O(1)
    public boolean checkIfPangram(String sentence) {
        int checker = 0;
        // Integers have 32 bits with 31 bits representing value and 1 bit representing sign
        for (int i = 0 ; i< sentence.length(); i++){
            // if we found the char we turn bit at location to 1
            // hence using 26 last bits of the integer
            int value = sentence.charAt(i)-'a';

            // left shift the integer and add to checker 
            // It will represent that the char is present at least once
            checker = checker | 1 << value; 
        }
        return checker == 67108863;
    }

    // TC : O(N);
    // SC : O(N)
    // We can also use array here but I thought of giving good solution
    public boolean checkIfPangramApproach2(String sentence) {
        HashSet<Character> tracker = new HashSet<>();

        for (int i = 0 ; i< sentence.length(); i++){
            tracker.add(sentence.charAt(i));
        }
        return tracker.size()==26;
    }
}
