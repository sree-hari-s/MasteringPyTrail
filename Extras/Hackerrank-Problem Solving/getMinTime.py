def getMinTime(task_memory, task_type, max_memory):
    task_dict = {}
    n = len(task_memory)
    
    # Create a dictionary mapping task types to a list of tasks with that type
    for i in range(n):
        if task_type[i] not in task_dict:
            task_dict[task_type[i]] = []
        task_dict[task_type[i]].append(task_memory[i])
    
    total_time = 0
    
    # Process tasks for each task type
    for tasks in task_dict.values():
        tasks.sort()  # Sort tasks within the same type by memory requirements
        left, right = 0, len(tasks) - 1
        
        while left <= right:
            if left == right:
                # Process the remaining task if there's only one left
                total_time += 1
                break
            
            if tasks[left] + tasks[right] <= max_memory:
                left += 1
                right -= 1
                total_time += 1
            else:
                # If the tasks require too much memory together, process the larger one alone
                right -= 1
                total_time += 1
    
    return total_time

# Example usage:
task_memory = [2, 3, 2, 4, 1, 1]
task_type = [1, 2, 2, 1, 1, 3]
max_memory = 4

result = getMinTime(task_memory, task_type, max_memory)
print("Minimum time required:", result)
