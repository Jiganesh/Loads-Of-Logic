class Solution {
    public boolean validMountainArray(int[] arr) {
        
        int inc = 0;
        int dec = 0;
        int len = arr.length;
        int i = 0;
        int f = 0;
        
        if(len < 3 || arr[1] <= arr[0])
              return false;
        
        
        for( i=0;i<len - 1;i++){
  
            if(arr[i + 1] > arr[i]){
                if(f == 0){
                    inc++;
                    f = 1;
                }
            }else if(arr[i + 1] < arr[i]){
                if(f == 1){
                dec++;
                 f = 0;
                }
            }else if(arr[i + 1] == arr[i])
                      return false;
            
        }
        
        if(inc > 1 || dec > 1)
              return false;
        else if(inc == 1 && dec == 1)
               return true;
        
        return false;
    }
}
