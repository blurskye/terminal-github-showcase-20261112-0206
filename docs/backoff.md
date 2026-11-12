# Clamp exponential backoff to sixty seconds

## Behavior

A long outage should not produce unbounded retry delays.

## Verification

Run the unit tests before merging. Source values and task identities must remain intact.
