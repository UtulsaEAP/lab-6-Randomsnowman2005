# Mohamad Ali fakhoury @ 2pm
def in_order(nums):
    x=0
    while x <= len(nums)-2:
        if nums[x] > nums[x+1]:
            return False
        else:
            x=x+1
    else:
        return True
    



    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
