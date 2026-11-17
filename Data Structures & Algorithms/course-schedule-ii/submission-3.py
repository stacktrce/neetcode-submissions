class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Graph bauen & Voraussetzungen zählen
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)   # pre schaltet crs frei
            indegree[crs] += 1     # crs hat eine Voraussetzung mehr

        # 2. Alle Kurse ohne Voraussetzungen in die Queue
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 3. Semester für Semester abarbeiten
        output = []
        while q:
            curr = q.popleft()
            output.append(curr)

            for next_course in adj[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        # Wenn alle Kurse im Output gelandet sind -> gültig, sonst Zyklus!
        return output if len(output) == numCourses else []