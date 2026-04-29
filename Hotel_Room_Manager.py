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