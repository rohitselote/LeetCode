class Solution {
    public int maximumValue(String[] strs) {
        int max =0;
        int[] store = new int[strs.length]; 
        for(int i=0;i<strs.length;i++){
            if(strs[i].matches("\\d+")){
               store[i]=(Integer.parseInt(strs[i])); 
            }
            else{
                store[i]=(strs[i].length());
            }
            max = Math.max(max, store[i]);
        }
        return max;
    }
}
