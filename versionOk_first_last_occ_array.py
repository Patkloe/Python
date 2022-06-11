def findFirstOccurrence(nums, target):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the target is located, update the result and
        # search towards the left (lower indices)
        if target == nums[mid]:
            result = mid
            right = mid - 1
 
        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1
 
        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    return result
  
  def findLastOccurrence(nums, target):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the target is located, update the result and
        # search towards the right (higher indices)
        if target == nums[mid]:
            result = mid
            left = mid + 1
 
        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1
 
        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    return result
 
