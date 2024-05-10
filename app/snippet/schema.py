from drf_spectacular.utils import extend_schema_view, extend_schema


class Documentation:
    """
    Utility class for document snippet related
    API endpoints
    """

    SNIPPET = extend_schema_view(
        list=extend_schema(
            summary="List all snippets",
            description="""
            List all snippets availabe in the system with pagination.
            Can search with title and tag title
            """,
            tags=["Snippets"],
        ),
        create=extend_schema(
            summary="Create a snippet",
            description="""
            Create a new snippet to the system.
            tag_name should be subimitted
            """,
            tags=["Snippets"],
        ),
        update=extend_schema(
            summary="Update a snippet",
            description="""
            Update asnippet in the system.
            Should be submit all details of snippet
            """,
            tags=["Snippets"],
        ),
        partial_update=extend_schema(
            summary="Update a snippet",
            description="""
            Update a snippet in the system.
            Only submit fields to be updated
            """,
            tags=["Snippets"],
        ),
        destroy=extend_schema(
            summary="Delete a snippet",
            description="""
            Delete a snippet from the system.
            """,
            tags=["Snippets"],
        ),
        retrieve=extend_schema(
            summary="Get details of a snippet",
            description="""
            This API returns the details of a specific snippet
            """,
            tags=["Snippets"],
        ),
    )

    TAGS = extend_schema_view(
        list=extend_schema(
            summary="List all tags",
            description="""
            List all tags availabe in the system
            with all snippets included in that tag and pagination.
            Can search with title
            """,
            tags=["Tag"],
        ),
        retrieve=extend_schema(
            summary="Get details of a tag",
            description="""
            This API returns the details of a tag with its snippets
            """,
            tags=["Tag"],
        ),
    )
