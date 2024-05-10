from drf_spectacular.utils import extend_schema_view, extend_schema


class Documentation:
    """
    Utility class for document snippet related
    API endpoints
    """

    LOGIN = extend_schema(
        summary="Login with password",
        description="""
        Users can use this api to login into the system.
        Both username and email canbe passed in username field.
        If successfully login access and refresh tokens returned
        """,
        tags=["Auth"],
    )

    SIGNUP = extend_schema(
        summary="Signup",
        description="""
        Users can use this api to create a new account.
        After successfull regsitration user need to login.
        """,
        tags=["Auth"],
    )

    REFRESH = extend_schema(
        tags=["Auth"],
        summary="API for refresh token",
        description="""
            refresh token should be
            pass as payload.
            If it is a valid token then a new
            access token should be return.
        """,
    )
