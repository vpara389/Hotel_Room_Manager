import csv
import random

columns = ["Room_Number", "Room_Type"]
room_types = ("Single King", "Double Queen", "One Bedroom Suite", "Jaccuzzi Suite")
filename = "Room_Report.csv"

written_rooms = set()
all_rooms = []

with open (filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    while len(written_rooms) < 144:
        first_num = random.randint(1, 4)
        second_num = random.randint(0, 3)
        third_num = random.randint(1, 9)
        
        r_num = f"{first_num}{second_num}{third_num}"

        if r_num not in written_rooms:
            r_type = random.choice(room_types)
            all_rooms.append({"Room_Type": r_type, "Room_Number": r_num})
            written_rooms.add(r_num)
        
    all_rooms.sort(key=lambda x: x["Room_Number"])
    for room in all_rooms:
        writer.writerow(room)

print(f"Created {len(written_rooms)} unique rooms in {filename}. ")