class Solution {
public:
    int Ways(int n, vector<int>& Steps) {
        if (n < 0)
            return 0;
        else if (n == 0)
            return 1;
        if (Steps[n - 1] != 0)
            return Steps[n - 1];

        Steps[n - 1] = Ways(n - 1, Steps) + Ways(n - 2, Steps);
        return Steps[n - 1];
    }
    int climbStairs(int n) {
        std::vector<int> Steps(n, 0);
        return Ways(n, Steps);
    }
};