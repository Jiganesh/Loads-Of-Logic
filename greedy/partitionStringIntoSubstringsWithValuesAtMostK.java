package greedy;

class partitionStringIntoSubstringsWithValuesAtMostK {
    public int minimumPartition(String s, int k) {
        
        long number = 0 ;
        int n = s.length();
        int result = 0;

        for (int i = 0 ; i< n; i++){
            number = number * 10 + (s.charAt(i)-'0');
            if (number > k){
                number = s.charAt(i)-'0';
                result +=1;
            }
            if (number > k){
                return -1;
            }
        }
        return result+1;
    }
}
