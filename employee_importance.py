"""
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
"""
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque


class Solution:
    def get_employee(self, id):
        # Given an id return the employee object
        return self.db.get(id)
    def get_subordinate_ids(self, id):
        # Given an id return a list of all subordinate ids
        emp = self.get_employee(id)
        return emp.subordinates
    def _create_db(self, employees):
        self.db = {}
        for emp in employees:
            self.db[emp.id] = emp
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        Vanialla BFS:
        1. Enque the employee id
        2. Deque and enqueu subordinates, at every enque keep track of cumulative importance
        By far the access pattern here is 
        a. id -> employee object
        b. id -> employee object --> subordinate_ids --> subordinate object
        To make these access easier, we create an internal dB which maps every "id" -> "employee object"
        This allows us to enque / deque ids saving a ton of space in the queque and makes id -> employee an O(1) [dict get] operation vs O(N) (list traversal)

        Notes: 
        1. Since you are only storing ids, you do not need to do anything if employee importance changes.
        2. What if reporting structure changes or employee leave, join... : You need to refresh the db
        
        """
        self._create_db(employees)
        q = deque()
        q.append(id)
        emp = self.get_employee(id)
        cum_imp = emp.importance
        while(len(q) > 0):
            emp_id = q.popleft()
            subordinate_ids = self.get_subordinate_ids(emp_id)
            for subordinate_id in subordinate_ids:
                q.append(subordinate_id)
                subordinate = self.get_employee(subordinate_id)
                cum_imp += subordinate.importance
        return cum_imp


        
