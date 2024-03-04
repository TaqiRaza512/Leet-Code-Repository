class Solution {
public:
    int TargetIndex(vector<int>&nums,int start,int end, int target)
    {
        int mid=(start+end)/2;
        if(nums[mid]==target)
            return mid;
        if(nums[mid]>target)
            end=mid;
        else if(nums[mid]<target)
            start=mid;
        
        if(end-start<=1)
        {
            if(nums[start]==target)
            {
                return start;
            }
            else if(nums[end]==target)
            {
                return end;
            }
            return -1;
        }
            
        return TargetIndex(nums,start,end,target);
    }
    int search(vector<int>& nums, int target) 
    {
        return TargetIndex(nums,0,nums.size()-1,target);
    }
};