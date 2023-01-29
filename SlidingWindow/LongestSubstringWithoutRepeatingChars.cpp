class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> substring;

        size_t left = 0;
        int maxLength = 0;
        for (int right = 0; right < s.size(); right++)
        {
            //as long as has duplicate, keep on pushinig left of window up (bc could be multiple of same letter)
            while (substring.find(s[right]) != substring.end())
            {
                //REMOVE LEFT BECAUSE CUTTING OFF LEFT PART, NOT JUST REPEAT OHHHH 
                substring.erase(s[left]);
                left++;
            
            }

            substring.insert(s[right]);
            int length = right - left + 1;
            if (length > maxLength)
            {
                maxLength = length;
            }

        }
        return maxLength;
    }
};
