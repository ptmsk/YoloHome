class AdafruitError(Exception):
    def __init__(self, message="Some errors happend when interacting with Adafruit server"):
        self.type = "AdafruitError"
        self.message = message
        super().__init__(self.message)

class RecordFindError(Exception):
    def __init__(self, record=None):
        self.type = "RecordFindError"
        self.record = record if record else ""
        self.message = "Cannot find record {}. Some errors happened when interacting with database".format(record)
        super().__init__(self.message)

class RecordNotFound(Exception):
    def __init__(self, record=None):
        self.type = "RecordNotFound"
        self.record = record if record else ""
        self.message = "Record {} not exist in document".format(record)
        super().__init__(self.message)

class RecordUpdateError(Exception):
    def __init__(self, record):
        self.type = "RecordUpdateError"
        self.record = record
        self.message = "Cannot update record {}. Some errors happened when interacting with database".format(record)
        super().__init__(self.message)

class RecordDeleteError(Exception):
    def __init__(self, record):
        self.type = "RecordDeleteError"
        self.record = record
        self.message = "Cannot delete record {}. Some errors happened when interacting with database".format(record)
        super().__init__(self.message)

class RecordInsertError(Exception):
    def __init__(self, record):
        self.type = "RecordInsertError"
        self.record = record
        self.message = "Cannot add record {}. Some errors happened when interacting with database".format(record)
        super().__init__(self.message)

class LackRequestData(Exception):
    def __init__(self, message="Not enough request data"):
        self.type = "LackRequestData"
        self.message = message
        super().__init__(self.message)

class Unauthorized(Exception):
    def __init__(self, message="Token is missing"):
        self.type = "Unauthorized"
        self.message = message
        super().__init__(self.message)

class AccessForbidden(Exception):
    def __init__(self, message="User forbidden to access the content"):
        self.type = "AccessForbidden"
        self.message = message
        super().__init__(self.message)