from fastapi import HTTPException, status


class NoTokenException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Required",
            headers={"WWW-Authenticate": "Bearer"},
        )


class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
