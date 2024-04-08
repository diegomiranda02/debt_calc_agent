class TaskManager:
    def __init__(self):
        self.tasks_status = {}

    def update_status(self, task_name, status):
        self.tasks_status[task_name] = status

    def should_execute(self, task_name):
        return not self.tasks_status.get(task_name, False)
