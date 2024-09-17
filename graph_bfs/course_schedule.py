from collections import defaultdict, deque
from typing import List

class CourseSchedule:
    def approach_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])
        
        visited = set()
        for course in range(numCourses):
            if not self.can_complete(course, courses, visited, set()):
                return False
        
        return True
    
    def approach_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        crs_in_degree = [0] * numCourses

        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])
            crs_in_degree[prerequisite[1]] += 1
        
        q = deque()

        for i in range(len(crs_in_degree)):
            if crs_in_degree[i] == 0:
                q.append(i)
        
        topo_order = []
        while q:
            curr_node = q.popleft()
            topo_order.append(curr_node)
            for neighbour in courses[curr_node]:
                crs_in_degree[neighbour] -=1
                if crs_in_degree[neighbour] == 0:
                    q.append(neighbour)
        
        return len(topo_order) == numCourses

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]], approach) -> bool:
        return approach(numCourses, prerequisites)
    
    def can_complete(self, course, courses, visited, rec_stack):
        if course in rec_stack:
            return False
        if course in visited: 
            return True
        rec_stack.add(course)
        res = True
        if course in courses:
            for cs in courses[course]:
                if not self.can_complete(cs, courses, visited, rec_stack):
                    res = False
                    break
        
        rec_stack.remove(course)
        visited.add(course)
        return res


course_obj = CourseSchedule()
approaches = [course_obj.approach_1, course_obj.approach_2]
prerequisites = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
numCourses = 6

print(course_obj.canFinish(numCourses, prerequisites, approaches[0])) # False
        