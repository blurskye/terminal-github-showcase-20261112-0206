# Recover queued tasks after worker reconnect

## Behavior

Reconnecting a worker can leave a queued task without an owner.

## Verification

Run the unit tests before merging. Source values and task identities must remain intact.
