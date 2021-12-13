package binarySearch;
public class reachANumber {
    public static void main(String[] args) {
        SolutionRAN  solution = new SolutionRAN();
        System.out.println(solution.reachNumber(5));
    }
}
class SolutionRAN {
    public int reachNumber(int target) {
        int sum =0 ,steps = 0;
        if(target ==0) return 0;
        target = Math.abs(target);
        while(sum< target){
            sum+=steps;
            steps++;
        }
        while(((sum-target)%2!=0)){
            sum+=steps;
            steps++;
        }
        return steps-1;

    }
}

/*
How the code will run  :

lets consider input is 5

We convert the target to its positive because the same number of steps will be needed to reach

-1  and 1 will need 1 move
-2 and 2 will need 3 move 

0 to 1 :1st move
1 to -1 : 2nd move
-1 to 2 : 3rd move same for -2 but in other way

that is why we use abs(target)


Now we move ahead till we pass target
sum= 1st move
sum after 2nd move = 3moves
sum after 3rd move = 6 moves 

6 moves are greater that target that means we have moved ahead from out target
Which also means that we should have had some numbers negative from our moves 1 + 2 + 3

Now we know that :
sum - 2(someNumber) = Target
because 1-2+3 will be same as 1+2+3 - 2*(2)

Then the next loop comes into picture
Now lets modify this equation
sum-target = 2(someNumber)
That means when we subtract target from sum our number should be multiple of 2 to satisfy the equation

sum =6 and target = 5
6-5 is not even we increase the step

4th move
sum = 10 and target =5
10 - 5 not even we increase the step
Internally how its working :
(1+2+3+4)-5 = 2(someNumber)
but the equation is not satisfied so lets move ahead

sum= 15 and target = 5
now the number is even so our equation is satisfied
Lets see what that number was:
(1+2+3+4+5) -5 = 2(someNumber)
(10-5) = 2 (someNumber)
someNumber = 5

so we can take either 4 and 1 and that would look like (-1+2+3-4 +5) we turn 1st and 4th move in opposite direction
which will be 0 t0 -1  1st move
then -1 to 1  2nd move
then 1 to 4 3rd move
then 4 to 0 4th move
then 0 to 5 5th move

Hence it will take 5 moves


You can also check with (1 -2 -3 +  4 + 5)
0 to 1 : 1st move
1 to -1 :2nd move
-1 to -4  : 3rd move
-4 to 0 : 4th move
0 to 5 : 5th move

Hence it will take 5 move
*/