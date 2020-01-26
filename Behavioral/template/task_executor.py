from Behavioral.template import AuditTrail
from Behavioral.template import GenerateReport
from Behavioral.template import Task


class TaskExecutor:
    def __init__(self, task: Task):
        self._task = task

    def execute(self):
        self._task.execute()


if __name__ == '__main__':
    audit = AuditTrail()
    gen_rep = GenerateReport(audit)
    task_exec = TaskExecutor(gen_rep)
    task_exec.execute()