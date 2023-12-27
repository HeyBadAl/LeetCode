# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # are there any specific condition or contrains we should consider!?
    k = k %n 

    n = len(nums)
    # reverse the entire array
    reverse(nums, 0, n - 1)

    # rever the first k element
    reverse(nums, 0, k - 1)

    # reverse the remaininig element
    reverse(nums, k, n - 1)

    # 7 6 5 4 3 2 1 -> 5 6 7 4 3 2 1 -> 5 6 7 1 2 3 4


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# what if k is greater than n?
# effective rotation value -> k=k%n => taking the reminder when dividing k by the length of the array (n)

# Time: O(n), where n is the length of the array. The three reverse operations each take linear time
# Space: O(1), rotating the array in-place without using any additional memory with the input size.
