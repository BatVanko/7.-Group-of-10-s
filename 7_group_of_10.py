group_of_nums = list(map(int, input().split(", ")))
num_of_groups = max(group_of_nums)

for i in range(10, num_of_groups + 10, 10):
    nums = []
    for el in group_of_nums:
        if el <= i:
            nums.append(el)
    print(f"Group of {i}'s: {nums}")
    group_of_nums = [el for el in group_of_nums if el not in nums]



