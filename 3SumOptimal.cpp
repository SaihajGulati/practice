class Solution {
    /**
 story (of problem in terms of what should do):
 return triplets of numbers that add up to zero
- input: array of ints
- output: vector of int vecctors
- Requirements: solution cannot have duplicate triplets
- Constraints that could help:
length of the inputted array is at max 3000
- Algo (thinking of): 
- two sum with for loop through sorted vector for first values
- sorted handles duplicates
*/


public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());

        for (size_t i = 0; i < nums.size(); ++i)
        {
            //must do continue way because otherwise it won't run for i=1, and need this case so that don't do with same first value and get duplicate cases
            if (i > 0 && nums[i] == nums[i-1])
            {
                continue;
            }
            
            int l = i + 1; 
            int r = nums.size()-1;

            while (l < r)
            {
                int threesum = nums[i] + nums[l] + nums [r];
                if (threesum > 0)
                {
                    r--;
                }

                else if (threesum < 0)
                {
                    l++;
                }

                else
                {
                    //vector<int> temp = {nums[i], nums[left], nums[right]};
                    output.push_back({nums[i], nums[l], nums[r]});

                    l++;
                    while (nums[l] == nums[l-1] && l < r)
                    {
                        l++;
                    }
                }
            }

            

        }
        return output;
    }
};