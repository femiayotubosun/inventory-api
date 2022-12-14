class APIError(Exception):
    """Base class for all API errors"""

    def __init__(self, message: str, status_code: int):
        self.status_code = status_code
        self.message = message
        super().__init__()


class ResourceNotFoundError(APIError):
    """Raised when resource is not found in database

    Database queries should raise this in Service or Repository

    :param message[optional]: An error message
    """

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


class ResourceExistsError(APIError):
    """
    Raised when post data fails unique constraints, and resource with data already exists in DB
    """

    def __init__(
        self,
        message: str = "Resource with this data already exists",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class SQLAlchemyError(APIError):
    def __init__(self, message: str = "Internal Server Error", status_code: int = 500):
        super().__init__(message, status_code)
