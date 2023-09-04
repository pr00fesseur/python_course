from typing import Generator
from uuid import UUID, uuid4

# The example of UUID v4
# e6bcb25d-0c5b-44a3-bc70-f04eddef067b

used_uuids_by_user: dict[str, set[UUID]] = {}
# {
#     "john": {2a518aab-d286-4c0f-a90d-b5a3b58fc5c2, ...}
#     "marry": {2a518aab-d286-4c0f-a90d-b5a3b58fc5c2, ...}
# }


def generate_unique_uuid_as_function(user: str) -> UUID:
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids_by_user[user]:
            used_uuids_by_user[user].add(generated_uuid)
            return generated_uuid


def generate_unique_uuid() -> Generator[UUID, None, None]:
    used_uuids: set[UUID] = set()
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            yield generated_uuid


john_unique_uuid = generate_unique_uuid()
marry_unique_uuid = generate_unique_uuid()

print(next(john_unique_uuid))
print(next(john_unique_uuid))
print(next(marry_unique_uuid))
print(next(marry_unique_uuid))
