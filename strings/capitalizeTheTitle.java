// https://leetcode.com/problems/capitalize-the-title/
package strings;

public class capitalizeTheTitle {
    public static void main(String[] args) {

        SolutionCTT solution = new SolutionCTT();
        System.out.println(solution.capitalizeTitle("capiTALiZe ThE stRIng"));
        System.out.println(solution.capitalizeTitleApproach2("capiTALiZe ThE stRIng"));
    }
}

class SolutionCTT {

    public String capitalizeTitle(String title) {

        String[] array=title.split(" ");
        StringBuilder sb = new StringBuilder();
        
        for (String i : array){
            if (i.length()<3) {
                sb.append(" "+i.toLowerCase());
            }
            else{
                sb.append(" "+i.substring(0, 1).toUpperCase()+i.substring(1).toLowerCase());
            } 
        }
        return sb.toString().substring(1);  
    }

    public String capitalizeTitleApproach2(String title) {

        String[] array=title.split(" ");
        
        for (int i =0 ; i<= array.length; i++){
            if (array[i].length()>2){
                array[i]= array[i].substring(0,1).toUpperCase()+array[i].substring(1).toLowerCase();
            }else{
                array[i]= array[i].toLowerCase();
            }
        }
        return String.join(" ", array) ; 
    }
}
