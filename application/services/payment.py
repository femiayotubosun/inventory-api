from dataclasses import dataclass


@dataclass
class InitializePaymentDTO:
    amount: float
    email: str
    first_name: str
    last_name: str


class PaymentService:
    @staticmethod
    def process_payment(*args, **kwargs):

        return True
