ROOM_TYPES = ("Single King", "Double Queen", "One Bedroom Suite", "Jaccuzzi Suite")
class Room:
  def __init__(self, room_number, room_type):
    self.room_number = room_number
    self.room_type = room_type
    self.is_occupied = False
    self.status = "✅"

  def __str__(self):
    return f"Room {self.room_number} - {self.room_type} : {self.status}"

  def check_in(self):
    self.is_occupied = True
    self.status = "🛌"

  def check_out(self):
    self.is_occupied = False
    self.status = "🧹"

while True:
  room_num = input("\nEnter room number (or q to exit): ")
  if room_num.lower() == "q":
    break
  
  
  print("\nBed Types")
  for i, r_type in enumerate(ROOM_TYPES, start=1):
    print(f"\n{i} = {r_type}")

  choice = int(input("\nSelect a number from the choices: ")) - 1
  g_room = Room(room_num, ROOM_TYPES[choice])

  while True:
    print(f"Current_room = {g_room}")
    try:
      action = input("\n1=CheckIn\n2=CheckOut\n3=SwitchRoom\nEnter action required: ")
    except ValueError:
      print("Invalid input!")

    if action == "1":
      g_room.check_in()
    elif action == "2":
      g_room.check_out()
    elif action == "3":
      break
    else:
      print("Invalid choice! Please try again... ")