from dataclasses import dataclass


@dataclass
class InitializePaymentDTO:
    amount: float
    email: str
    first_name: str
    last_name: str


class PaymentService:
    @staticmethod
    def initialize_payment(dto: InitializePaymentDTO):
        amount = dto.amount
        email = dto.email
        first_name = dto.first_name
        last_name = dto.last_name

        return True
