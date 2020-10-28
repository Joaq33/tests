# These are some handy functions to enhance the programming experience
def bsearch(self, nums: List[int], target: int) -> int:
    """
    Best binary search time complexity.
    :param self:
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums)-1
    while left <= right:
        pivot = (left + right)//2
        if target == nums[pivot]:
            return pivot
        if target > nums[pivot]:
            left = pivot+1
        else:
            right = pivot-1
    return -1

def bfs(self, root: TreeNode) -> int:
    """
    extraido de minimum depth of binary tree
    PROBABLEMENTE MEJOR Q EL DE ABAJO
    :param self:
    :param root:
    :return:
    """
    if not root: return 0
    queue = [root]
    level = 1
    while queue:
        next_queue = []
        for node in queue:
            if not node.left and not node.right:
                return level
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
        level += 1
    return level
def BFS(self, s):
    """
    Breadth First Search
    PROBABLEMENTE PEOR Q EL DE ARRIBA(mucho)
    :param self:
    :param s:
    :return:
    """
    from collections import deque
    # Mark all the vertices as not visited
    visited = [False] * (len(self.graph))

    # Create a queue for BFS
    queue = deque()

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.popleft()
        print(s, end=" ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def reverse(nums, start, end):
    """
    Reverse a list.
    :param nums:
    :param start:
    :param end:
    :return:
    """
    while start < end:
        nums[start], nums[end - 1] = nums[end - 1], nums[start]
        start += 1
        end -= 1

def linked_to_list(head: ListNode):
    """
    Convert a linked list into a list.
    :param head:
    :return:
    """
    ans = [head.val]
    cur = head
    while cur.next:
        cur = cur.next
        ans.append(cur.val)
    return ans


def list_to_linked(list: []):
    """
    Convert a list into a linked list.
    :param list:
    :return:
    """
    head = ListNode(list[0])
    cur = head
    for item in list[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head