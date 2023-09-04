import sys

users: list[str] = ["john", "marry", "jack", "john", "marry", "mark"]

# users_seen = set()
# for user in users:
#     if user in users_seen:
#         continue
#     users_seen.add(user)
#     print(user)


def dedup(collection):
    items = set()
    for item in collection:
        if item in items:
            continue
        yield item
        items.add(item)


# for user in dedup(users):
#     print(user)

print(sys.getsizeof(users))
