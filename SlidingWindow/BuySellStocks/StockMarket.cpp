class Solution {
public:
/*
- story (of problem in terms of what should do): find max difference between two numbers
- input: array      
- output: max profit (positive difference) or 0 if no positive difference exists
- Requirements: IMPORTANT ESP EDGE CASES
- Constraints that could help:
- 

- Algo (thinking of): sliding window (max and left and right)
*/
    int maxProfit(vector<int>& prices) {

        //since starts at 0, will return 0 if not profit
        int maxProfit = 0;
        size_t left = 0;
        size_t right = 1;

        while (right < prices.size())
        {
            int profit = prices[right]-prices[left];
            if (prices[left] > prices[right])
            {
                left = right;
            }
            else if (profit > maxProfit)
            {
                maxProfit = profit;
            }
            right++;
        }

        return maxProfit;
    }
};
