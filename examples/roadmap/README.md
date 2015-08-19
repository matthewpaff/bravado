# Swagger client lifecycle

This snapshot predates the `bravado` package name and uses `swaggerpy`.
`client_session(resource, http_client)` closes the client in a `finally` block.
The two source corrections preserve explicit zero/false parameters and fix unsupported-type error formatting.

See RECONSTRUCTION.md for provenance and verification limits.
