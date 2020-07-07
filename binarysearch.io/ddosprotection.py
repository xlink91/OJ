# problem_url: https://binarysearch.io/problems/DDoS-Protection

from functools import cmp_to_key
from collections import deque

class Solution:
    def solve(self, requests, u, g):
        # Write your code here
        if u * g == 0: return 0
        
        requests = sorted(requests, key=cmp_to_key(self.cmp))
        req_p = 0
        global_qt = deque()
        local_qt_map = {}
        for rq in requests:
            _id, _ = rq
            if _id not in local_qt_map:
                local_qt_map[_id] = deque()
            gl = self.check_global(rq, g, global_qt)
            lc = self.check_local(rq, u, local_qt_map[_id])
            if gl and lc:
                req_p += 1
                self.insert_qt(rq, g, global_qt)
                self.insert_qt(rq, u, local_qt_map[_id])
        return req_p
    
    def cmp(self, x, y):
        if x[1] != y[1]:
            return x[1] - y[1]
        return x[0] - y[0]

    def insert_qt(self, rq, mx, qt) -> None:
        if len(qt) == mx:
            qt.popleft()
        qt.append(rq)

    def check_global(self, rq, g, gl) -> bool:
        if not gl:
            return True

        _, sec = rq
        _, tp_sec = gl[0]
        if sec - tp_sec < 60 and len(gl) == g:
            return False
        return True

    def check_local(self, rq, l, lc) -> bool:
        if not lc:
            return True

        _, sec = rq
        _, tp_sec = lc[0]
        if sec - tp_sec < 60 and len(lc) == l:
            return False
        return True
