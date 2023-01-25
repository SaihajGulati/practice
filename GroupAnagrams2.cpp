class Solution {
public:
/**
- story (of problem in terms of what should do): take in list and then spit out list of lists of anagrams paired up
- input: list of strings
- output: list of list of strings
- Requirements: no matter, what returns a list of lists
- Algo (thinking of): go through, sort letters in string, if matches sorted version, than add to hash table, otherwise create new list 
*/
    vector<vector<string>> convertToVector(map<array<int, 26>, vector<string>> stuff)
    {
        map<array<int, 26>, vector<string>>::iterator it;
        vector<vector<string>> output;
        for (it = stuff.begin(); it != stuff.end(); ++it)
        {
            output.push_back(it->second);
        }
        return output;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //will be hash table that has sorted string as key and then value is list of strings that are it's anagram


        map<array<int, 26>, vector<string>> anagrams;

        for (int i = 0; i < strs.size(); ++i)
        {
            array<int, 26> letters = {0};
            string word = strs[i];

            //uses array to track letters
            for (int j = 0; j < word.length(); ++j)
            {
                letters[word[j]-'a']++;
            }

            //map<array<int, 26>, vector<string>>::iterator it = anagrams.find(letters);
            //if find the sorted string in the hashtable, means need to add to list
            /*if (it != anagrams.end())
            {
                it->second.push_back(word);
            }

            //else didn't find and so need to add new key and vector pair in map
            else
            {
                vector<string> temp;
                temp.push_back(word);
                anagrams[letters] = temp;
            }*/

            anagrams[letters].push_back(word);

        }
        return convertToVector(anagrams);
        
    }
};