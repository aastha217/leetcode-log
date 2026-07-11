class Solution {
public:
    int n, m;
    vector<vector<int>>cnt;
    void incriment(int row, int col)
    {
        for(int i=0;i<n;i++) cnt[i][col]++;
        for(int i=0;i<m;i++) cnt[row][i]++;
    }
    int oddCells(int mm, int nn, vector<vector<int>>& indices) 
    {
        n = mm, m = nn;
        cnt.resize(n, vector<int>(m));
        for(auto x:indices)
            incriment(x[0], x[1]);

        int ans = 0;
        for(auto vec:cnt)
            for(auto val:vec)
                if(val%2) ans++;
        return ans;
    }
};