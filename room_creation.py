import csv
import random

columns = ["Room_Number", "Room_Type"]
room_types = ("Single King", "Double Queen", "One Bedroom Suite", "Jaccuzzi Suite")
filename = "Room_Report.csv"

written_rooms = set()

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
            writer.writerow({"Room_Type": r_type, "Room_Number": r_num.sort()})

            written_rooms.add(r_num)

print(f"Created {len(written_rooms)} unique rooms in {filename}. ")