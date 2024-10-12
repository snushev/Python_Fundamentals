rooms = int(input())
total_chairs = 0
used_chairs = 0
for room in range(rooms):
    chairs = input().split()
    chairs_available = int(len(chairs[0]))
    chairs_needed = int(chairs[1])
    total_chairs += chairs_available
    used_chairs += chairs_needed
    if chairs_available < chairs_needed:
        print(f"{chairs_needed - chairs_available} more chairs needed in room {room + 1}")
if total_chairs >= used_chairs:
    print(f"Game On, {total_chairs - used_chairs} free chairs left")