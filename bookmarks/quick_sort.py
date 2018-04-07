def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    boundary_index = 1
    for x in nums[1:]:
        if x <= nums[0]:
            nums[nums.index(x)], nums[boundary_index] = nums[boundary_index], nums[nums.index(x)]
            boundary_index += 1
    nums[0], nums[boundary_index-1] = nums[boundary_index-1], nums[0]
    return quick_sort(nums[:boundary_index])+quick_sort(nums[boundary_index:])


def main():
    nums = [6, 7, 9, 2, 3, 4, 1, 5, 8, 10]
    # nums1 =[1]
    print(quick_sort(nums))
    # print(quick_sort(nums1))


if __name__ == '__main__':
    main()
