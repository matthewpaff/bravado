# Modern historical reconstruction, created 2026-11-04.
from contextlib import contextmanager
from swaggerpy.client import SwaggerClient

@contextmanager
def client_session(resource, http_client=None):
    """Close a historical Swagger client even when a caller raises."""
    client = SwaggerClient(resource, http_client=http_client)
    try:
        yield client
    finally:
        client.close()
