class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using two points
        count_list = []  # 用于记录每个元素重复的次数
        i = 0
        while i < len(nums):
            count = 1  # ！！！每个元素的重复计数，初始化为1（包括自己）
            j = i + 1
            # i是第一个指针，j是第二个指针
            while j < len(nums):
                if nums[i] == nums[j]:
                    count += 1  # 如果遇到重复的元素，计数增加
                    nums.pop(j)  # 删除第j个元素
                else:
                    j += 1  # 只有在没有删除元素的情况下，j指针才移动
            count_list.append(count)  # 将当前元素的重复计数添加到列表中
            i += 1  # 移动i指针，指向下一个元素

        res = []
        for n in range(k):
            max_count = max(count_list)  # 找到最大重复次数
            index_num = count_list.index(max_count)  # 找到最大重复次数对应的元素索引
            res.append(nums[index_num])  # 将该元素加入结果列表
            count_list.pop(index_num)  # 移除已添加到结果中的元素的次数
            nums.pop(index_num)  # ！！！移除已添加到结果中的元素，注意pop中（index而不是value）
        return res


'''
 # 统计每个元素的频率
        count = Counter(nums)
        # 使用heapq的nlargest方法找到频率最高的k个元素
        return heapq.nlargest(k, count.keys(), key=count.get)
'''


