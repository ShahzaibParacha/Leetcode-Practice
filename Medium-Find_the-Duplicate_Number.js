'use strict';
var findDuplicate = function(nums) {
    var slow = nums[0]
    var fast = nums[0]

    while(true) {
        fast = nums[nums[fast]];
        slow = nums[slow];
        if (nums[fast] === nums[slow]) {
            break;
        }
    };

    slow = nums[0];
    while (fast != slow) {
        slow = nums[slow];
        fast = nums[fast];
    }
        
    return slow;
};

//checking git commit

var nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,5];
console.log(findDuplicate(nums));

/* PYTHON 3 SOLUTION:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
                
        slow = nums[0]
        fast = nums[0]
        
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow;
*/