class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)

            for pre in preReq[course]:
                if not dfs(pre):          # 1. "pre" statt "preReq"
                    return False

            cycle.remove(course)          # 2. Auf Höhe der for-Schleife!
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output                     # 3. Nach der for-Schleife!