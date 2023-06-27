class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> u;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (u.find(nums[i]) == u.end())
            {
                u.insert(nums[i]);
            }

            else return true;
        }
        return false;
    }
};
