/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* FormingBST(vector<int> nums,int start,int end)
    {
        if(start>end)
            return nullptr;

        int mid=(start+end)/2;
        TreeNode* node = new TreeNode(nums[mid]);

        node->left=FormingBST(nums,start,mid-1);
        node->right=FormingBST(nums,mid+1,end);
        return node;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int start=0;
        int end=nums.size()-1;
        return FormingBST(nums,start,end);
    }
};