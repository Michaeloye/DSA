# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentMap = {0: 0, 1: 0}
        res = len(students)

        for stud in students:
            studentMap[stud] += 1

        for s in sandwiches:
            if studentMap[s] > 0:
                res -= 1
                studentMap[s] -= 1
            else:
                return res
        return res