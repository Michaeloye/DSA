# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ROWS = m
        COLS = n

        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        direction = "r" # r, d, l, u (right, down, left, up)
        
        r = 0
        c = 0

        visited = set([(0, 0)])
        total = m * n -1

        matrix[r][c] = head.val

        while total >= 0:
            if direction == "r":
                if c == COLS - 1 or (r, c + 1) in visited:
                    direction = "d"
                else:
                    c += 1
                    head = head.next
                    if not head:
                        return matrix
                    matrix[r][c] = head.val

            if direction == "d":
                if r == ROWS - 1 or (r + 1, c) in visited:
                    direction = "l"
                else:
                    r += 1
                    head = head.next
                    if not head:
                        return matrix
                    matrix[r][c] = head.val

            if direction == "l":
                if c == 0 or (r, c - 1) in visited:
                    direction = "u"
                else:
                    c -= 1
                    head = head.next
                    if not head:
                        return matrix
                    matrix[r][c] = head.val
            
            # direction "u" is a 'special' case because when we want to transition from up to right, 
            # we need to update our c pointer to point to the next column, 
            # since the loop re-iterates after we handle direction "u" same reason for head
            if direction == "u":
                if r == 0 or (r - 1, c) in visited:
                    direction = "r"
                    c += 1
                    head = head.next
                else:
                    r -= 1
                    head = head.next

                if not head:
                    return matrix

                matrix[r][c] = head.val

            visited.add((r, c))
            total -= 1
        return matrix
