package maths;

public class addDigits{
    public static void main(String[] args) {
        SolutionAD solution = new SolutionAD();
        System.out.println(solution.addDigits(38));
    }
}

class SolutionAD {
    public int addDigits(int num) {
        
        while (num>9){
            
            int newnum =0;
            
            while(num>0){
                newnum+= num%10;
                num = num/10;
            }
            
            num = newnum;
        }
        
        return num;    
    }
}