from abc import ABC, abstractmethod

from Behavioral.template import AuditTrail


class Task(ABC):

    def __init__(self, audit_trail: AuditTrail):
        self._audit_trail = audit_trail

    def execute(self):
        self._audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass
