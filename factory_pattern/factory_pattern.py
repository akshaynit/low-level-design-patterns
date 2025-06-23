'''
This example demonstates how to implement factory pattern.
'''

from abc import ABC

'''
Operation base class.
'''
class Operation(ABC):

    def __init__(self, name):
        pass

    def perform_operation(self):
        pass

'''
Operation to add something.
'''
class Add(Operation):

    def __init__(self):
        self.name = "add"
    
    def perform_operation(self):
        print("performing add operation")

'''
Operation to delete something.
'''
class Delete(Operation):

    def __init__(self):
        self.name = "delete"
    
    def perform_operation(self):
        print("performing delete operation")

'''
Operation to update something.
'''
class Update(Operation):

    def __init__(self):
        self.name = "update"
    
    def perform_operation(self):
        print("performing update operation")

'''
Function to create the object based on operation name and return it.
'''
def get_operation(operation_name) -> Operation:

    if operation_name == "add":
        return Add()
    elif operation_name == "delete":
        return Delete()
    elif operation_name == "update":
        return Update()

'''
Main code
'''
def perform_operations(operation_name):

    operation = get_operation(operation_name)
    operation.perform_operation()

perform_operations("add")
