class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task,0)+1
        #print(task_map)
        #task_map.items(), key=lambda x: x[1], reverse=True
        #task_map = sorted(task_map.items(), key=lambda x:x[1], reverse = True)
        task_map = sorted(task_map.items(),key = lambda x:x[1], reverse = True)
        max_task_count = task_map[0][1]
        res = (max_task_count-1)*(n+1)
        #print(res)
        for task in task_map:
            if task[1]==max_task_count:
                res+=1
                #print("res:",res)
        return res if res>=len(tasks) else len(tasks)