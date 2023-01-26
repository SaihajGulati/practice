class Solution {
public:
/**
- story (of problem in terms of what should do): take in list and then spit out list of lists of anagrams paired up
- input: list of strings
- output: list of list of strings
- Requirements: no matter, what returns a list of lists
- Algo (thinking of): go through, sort letters in string, if matches sorted version, than add to hash table, otherwise create new list 
*/
    vector<vector<string>> convertToVector(unordered_map<string, vector<string>> stuff)
    {
        unordered_map<string, vector<string>>::iterator it;
        vector<vector<string>> output;
        for (it = stuff.begin(); it != stuff.end(); ++it)
        {
            output.push_back(it->second);
        }
        return output;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //will be hash table that has sorted string as key and then value is list of strings that are it's anagram
        unordered_map<string, vector<string>> sortedStrings;

        for (int i = 0; i < strs.size(); ++i)
        {
            //copies the original word since sort sorts the referenced object
            string word = strs[i];
            sort(strs[i].begin(), strs[i].end());


            unordered_map<string, vector<string>>::iterator it = sortedStrings.find(strs[i]);
            //if find the sorted string in the hashtable, means need to add to list
            /*if (it != sortedStrings.end())
            {
                it->second.push_back(word);
            }

            //else didn't find and so need to add new key and vector pair in map
            else
            {
                vector<string> temp;
                temp.push_back(word);
                sortedStrings[strs[i]] = temp;
            }*/

            sortedStrings[strs[i]].push_back(word);

        }
        return convertToVector(sortedStrings);
        
    }
};
