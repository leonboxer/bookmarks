def quick_sort(nums):
    for x in nums:
        nums.remove(x)


def main():
    nums = [6, 7, 9, 2, 3, 4, 1, 5, 8, 10]
    # nums1 =[1]
    print(nums)
    print(quick_sort(nums))
    # print(quick_sort(nums1))


if __name__ == '__main__':
    main()
