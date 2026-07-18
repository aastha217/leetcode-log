class Solution {
public:
    int balancedStringSplit(string s) {
        int ans=0;
        int countR = 0;
        int countL = 0;
        for(char ch:s){
            if(ch == 'R')
                countR++;
            else if(ch=='L')
                countL++;
            if(countR==countL){
                ans++;
                countR = countL = 0;
            }
        }
        return ans;
    }
};