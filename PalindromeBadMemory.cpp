class Solution {
public:
/**
 story (of problem in terms of what should do):
- input: string s of ascii characters
- output: boolean of whether is palindrome
- Requirements: need to make sure that convert to lowercase and remove all punctuation
- Constraints that could help:
- Algo (thinking of): 
two pointers, one going forward and one going back and comparing each time if is same
*/
    //functor to meet requirement to get rid of punctuation and uppercase
    string clean(string const& stuff) {
        string cleaned;
        for (auto in = stuff.begin(); in != stuff.end(); ++in)
        {
            if (*in <= 'Z' && *in >= 'A')
            {
                cleaned += tolower(*in);
            } 
            else if (*in <= '9' && *in >= '0' || *in <= 'z' && *in >= 'a')
            {
                cleaned += *in;
            }
        }
        //else is punctuation trying to cut out
        return cleaned;
    }

    bool isPalindrome(string stuff) {
        //transform starting at s.begin() and ending at s.end, make the output begin at s.begin(), use clean
        string s = clean(stuff);
        cout << s << endl;
        int start = 0; 
        int end = s.length()-1;
        //will go until go past each other (if odd, ex. lol, yup works)
        while (start < end)
        {
            if (s[start] != s[end])
            {
                return false;
            }
            start++;
            end--;
        }

        return true;    
    }
};