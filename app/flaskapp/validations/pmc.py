from validations.validations import Validation

valid = Validation()

class ValidationPmc:
    def __init__(self):
        self = self

    def yesterday_atl(self, request: any):
        if valid.required(request) and valid.num(request) and valid.max(request, 2400) and valid.min(request, 0):
            return False
        else:
            return True

    def yesterday_ctl(self, request: any):
        if valid.required(request) and valid.num(request) and valid.max(request, 2400) and valid.min(request, 0):
            return False
        else:
            return True

    def current_tss(self, request: any):
        if valid.required(request) and valid.num(request) and valid.max(request, 2400) and valid.min(request, 0):
            return False
        else:
            return True
