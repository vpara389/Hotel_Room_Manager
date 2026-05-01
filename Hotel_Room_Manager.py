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
  
  try:
    choice = int(input("\nSelect a number from the choices: ")) - 1
    if choice <0 or choice >= len(ROOM_TYPES):
      print("That number is not in the list! ")
      continue
  except ValueError:
    print("Invalid input!!!")
    continue
  g_room = Room(room_num, ROOM_TYPES[choice])

  while True:
    print(f"Current_room = {g_room}")
    action = input("\n1=CheckIn\n2=CheckOut\n3=SwitchRoom\nEnter action required: ")

    match action:
      case "1":
        g_room.check_in()
      case "2":
        g_room.check_out()
      case "3":
        break
      case _:
        print("Invalid choice!! Try again. ")