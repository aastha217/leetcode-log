class Solution {
public:

    vector<int> decompressRLElist(
        vector<int>& nums) {

        int n = nums.size() / 2;

        vector<int> ans;

        for(int i = 0; i < n; i++) {

            int f = nums[2*i];

            int val = nums[2*i + 1];

            vector<int> temp(f, val);

            ans.insert(ans.end(),
                       temp.begin(),
                       temp.end());
        }

        return ans;
    }
};