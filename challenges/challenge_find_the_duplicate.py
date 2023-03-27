def find_duplicate(nums):
    if nums is None or type(nums) == 'str':
        return False
    ran = len(nums)
    sort = sorted(nums)
    num = 0
    for a in range(0, ran - 1):
        if sort[a] == sort[a + 1]:
            num = sort[a]
    if num <= 0:
        return False
    return num
