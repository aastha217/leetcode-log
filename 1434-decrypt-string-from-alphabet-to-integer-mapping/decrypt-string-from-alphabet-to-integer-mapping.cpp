class Solution {
public:
    string freqAlphabets(string s) {
        string ans = "";
        int n = s.size();
        int i = 0;
        while (i < n) {
            if (s[i] == '#')
                i++;
            else if (i + 2 < n && s[i + 2] == '#') {

                string k = "";
                k += s[i];
                k += s[i + 1];
                int val = stoi(k);
                ans += ('a' + (val - 1));
                i += 2;
            } else if (i + 3 < n && s[i + 3] == '#') {
                char c1 = 'a' + (s[i] - '1');
                ans += c1;
                i++;
            } else {
                char c1;
                char c2;
                c1 = 'a' + (s[i] - '1');
                if (i + 1 < n)
                    c2 = 'a' + (s[i + 1] - '1');
                ans += c1;
                if (i + 1 < n)
                    ans += c2;
                i += 2;
            }
        }
        return ans;
    }
};