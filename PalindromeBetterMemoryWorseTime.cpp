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
    //check if is alphanumeric
    bool isValid(char in) {
        return (in <= 'Z' && in >= 'A') || (in <= '9' && in >= '0') || (in <= 'z' && in >= 'a');
    }

    bool isPalindrome(string s) {
        //transform starting at s.begin() and ending at s.end, make the output begin at s.begin(), use clean
        int front = 0; 
        int back = s.length()-1;

        //will go until collide 
        while (front < back)
        {
            if (!isValid(s[front]))
            {
                front++;
            }
            else if (!isValid(s[back]))
            {
                back--;
            }

            //if get here then is valid, so check
            else if (tolower(s[front]) != tolower(s[back]))
            {
                cout << "failed when " << s[front] << " " << s[back] << endl;
                return false;
            }

            //else is palindrome so far so move on, put else to be safe but also need here since no return in all of rest
            else
            {
                cout << s[front] << " " << s[back] << endl;
                front++;
                back--;
            }

        }

        return true;    
    }
};