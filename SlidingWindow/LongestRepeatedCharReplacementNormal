class Solution {
public:
/*
    - input: string and integer k
    - output: length of longest substring of same character possible with only k changes made
    - requirements: at most k changes, needs to be longest possible one that return length of
    - constraints that could help: k is between 0 and s.length so don't have to handle that case, and only uppercase letters have to worry about
    - algo (thinking of): sliding window with decrementing copy of k when change and then if get
*/
    int characterReplacement(string s, int k) {
        int count[26] = {0};
        int maxLength = 0;
        int left = 0;

        //go through whole list, end when right overflow (left handled by fact that never goes past right)
        for (int right  = 0; right < s.size(); ++right)
        {
            //increase count of letter since you just saw it
            count[s[right]-'A']++;

            //if length - count of max leads to us needing to do more than k changes, need to adjust window, and keep adjusting until valid again
            while (right - left + 1 - *max_element(count, count+26) > k)
            {
                count[s[left]-'A']--;
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
