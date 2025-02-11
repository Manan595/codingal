def multiple_tuple(nums):
    temp=list(nums)
    product = 1
    for x in temp:
        product*= x
    return product 
nums = (4,3,2,2,-1,18)
print("Oringinal Tuple:")
print(nums)
print("product-multiplying all numbers of the said tuple:",multiple_tuple(nums))

nums=(2,4,8,8,3,2,9)
print(" \n Original tuple: ")
print(nums)
print("product-multiplying all numbers of the said tuple:",multiple_tuple(nums))