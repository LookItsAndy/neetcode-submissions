class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            //check index i if it has duplicate
            for (int j = 0; j < nums.length; j++) {
                if (j == i)
                    continue;
                if (nums[j] == nums[i]) 
                    return true;
            }
        }
        return false;
    }


}