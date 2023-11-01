from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        # 树的构建
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        geneSet = set()  # 基因库
        visited = [False] * n  # 节点访问标记

        def dfs(_node):
            if visited[_node]:
                return
            visited[_node] = True
            geneSet.add(nums[_node])
            for child in children[_node]:
                dfs(child)

        node = nums.index(1) if 1 in nums else -1
        res, iNode = [1] * n, 1

        while node != -1:
            dfs(node)
            while iNode in geneSet:
                iNode += 1
            res[node], node = iNode, parents[node]
        return res


s = Solution()
print(s.smallestMissingValueSubtree([-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3]))
