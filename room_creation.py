import csv
import random

columns = ["Room_Number", "Room_Type"]
room_types = ("Single King", "Double Queen", "One Bedroom Suite", "Jaccuzzi Suite")
filename = "Room_Report.csv"

with open (filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for floor in range(1, 5):
        for room in range(1, 39):
            room_number = f'{floor}{room:02d}'
            r_type = random.choice(room_types)
            writer.writerow({"Room_Number": room_number, "Room_Type": r_type})

print(f"Created rooms for 4 floors in {filename}. ")