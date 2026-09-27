def search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

if search(nums, target):
    print("True")
else:
    print("False")