class Solution {

    //this way passes every test case but TOO SLOW 
    /**
 story (of problem in terms of what should do):
 return triplets of numbers that add up to zero
- input: array of ints
- output: vector of int vecctors
- Requirements: solution cannot have duplicate triplets
- Constraints that could help:
length of the inputted array is at max 3000
- Algo (thinking of): 
- three pointers
two pointers, one going forward and one going back and comparing each time if is same
*/
struct VectorHash {
    size_t operator()(const std::vector<int>& v) const {
        std::hash<int> hasher;
        size_t seed = 0;
        for (int i : v) {
            seed ^= hasher(i) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        }
        return seed;
    }
};

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_set<vector<int>, VectorHash> list;
        int one = 0;
        int two = 1;
        int three = 2;
        sort(nums.begin(), nums.end());
        int countDupl = 0;

        while (one < nums.size()-2)
        {
            //if tried all seconds for this first, move first one up
            if (two >= nums.size()-1)
            {
                one++;
                two = one + 1;
                three = two + 1;
            }

            //otherwise if tried all different third values for this first and second and have now overflow
            else if (three >= nums.size())
            {
                two++;
                three = two + 1;
            }
            
            //otherwise if we got a triplet, handle it
            else if (nums[one] + nums[two] + nums[three] == 0)
            {
                
                vector<int> temp {nums[one], nums[two] , nums[three]};
                sort(temp.begin(), temp.end());
                list.insert(temp);
                two = two + 1; //to clear getting triplets already in set
                three = two + 1;
            }

            //otherwise move up the third
            else
            {
                three++;
            }
        }

        vector<vector<int>> output(list.begin(), list.end());
        return output;
    }
};
