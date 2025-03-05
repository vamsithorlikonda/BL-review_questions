def Every_third(nums):
    i=2
    while nums:
        i=i%len(nums)
        print(nums.pop(i))
        i+=2
    return nums
nums=[10,20,30,40,50,60,70]
Every_third(nums)
    
