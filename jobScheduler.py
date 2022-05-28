# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
def scheduler(f, n):
    time.sleep(n)
    f()
    
from time import sleep, time
class Scheduler:
    def __init__(self):
        self.functions = []
        thread = threading.Thread(target=self._poll)
        thread.start()
    def _poll(self):
        while True:
            now = time() * 1000
            if len(self.functions) > 0:
                due, func, args, kwargs = self.functions[0]
                if now > due:
                    func(*args, **kwargs)
                self.functions = [(due, func, args, kwargs) for due, func, args, kwargs in self.functions if due < now]
            sleep(0.01)
    def schedule(self, func, n, *args, **kwargs):
        heapq.heappush(self.functions, (n + time() * 1000, func, args, kwargs))
        
import heapq
import threading
from time import sleep, time
class Scheduler:
    def __init__(self):
        self.functions = []
        heapq.heapify(self.functions)
        thread = threading.Thread(target=self._poll)
        thread.start()
    def _poll(self):
        while True:
            now = time() * 1000
            if len(self.functions) > 0:
                due, func, args, kwargs = self.functions[0]
                if now > due:
                    func(*args, **kwargs)
                    heapq.heappop(self.functions)
            sleep(0.01)
    def schedule(self, func, n, *args, **kwargs):
        heapq.heappush(self.functions, (n + time() * 1000, func, args, kwargs))