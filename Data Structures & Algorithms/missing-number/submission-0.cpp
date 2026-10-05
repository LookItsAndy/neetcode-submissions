class Solution {

public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int expected = (n*(1+n)) / 2;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }



        return (expected - sum);

    }
};
