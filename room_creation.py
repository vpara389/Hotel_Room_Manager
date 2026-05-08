import csv
import random

columns = ["Room_Number", "Room_Type"]
room_types = ("Single King", "Double Queen", "One Bedroom Suite", "Jaccuzzi Suite")
filename = "Room_Report.csv"

with open (filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for floor in range(int(input("Enter the starting floor number: ")), int(input("Enter the ending floor number: "))+1):
        for room in range(int(input("Enter the starting room number: ")), int(input("Enter the ending room number: "))+1):
            room_number = f'{floor}{room:02d}'
            r_type = random.choice(room_types)
            writer.writerow({"Room_Number": room_number, "Room_Type": r_type})

print(f"Created rooms for 4 floors in {filename}. ")