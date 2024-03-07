class Solution 
{
public:
    void reverse(ListNode*& Reversehead, ListNode* head, ListNode* HeadNext)
    {
        if (!head)
            return;
        if (!HeadNext)
        {
            Reversehead = head;
            return;
        }
        reverse(Reversehead, HeadNext, HeadNext->next);
        HeadNext->next = head;
    }

    ListNode* reverseList(ListNode* head) 
    {
        if (!head)
            return nullptr;
        
        ListNode* Reversehead = nullptr;
        reverse(Reversehead, head, head->next);
        head->next = nullptr; // set the next of the original head to nullptr to make it the last node
        return Reversehead;
    }
};
