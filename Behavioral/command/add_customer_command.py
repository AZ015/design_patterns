from Behavioral.command.customer_service import CustomerService
from Behavioral.command.elements import Command


class AddCustomerCommand(Command):

    def __init__(self, customer_service: CustomerService):
        self._customer_service = customer_service

    def execute(self):
        self._customer_service.add_customer()
