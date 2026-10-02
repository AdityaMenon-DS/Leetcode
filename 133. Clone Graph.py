class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        seen = {}

        def dfs(x):
            if x in seen:
                return seen[x]

            copy = Node(x.val)
            seen[x] = copy

            for nei in x.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)