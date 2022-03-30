class C8Memory:
  def __init__(self) -> None:
    self.id = 0x001
    self.name = "Chip-8 Memory"
    self.capacity = 0xFFF
    self.reserved = [0x000, 0x1FF]
    self.start = 0x200
    self.RAM = [0] * self.capacity
    self.read_only = False

  def clear_memory(self, clear_reserved: bool = False) -> None:
    if not self.read_only:
      if clear_reserved:
        self.RAM = [0] * self.capacity
        return
      else:
        self.RAM[self.reserved[1] + 1:] = [0] * (self.capacity - self.reserved[1] - 1)

  def display_info(self) -> None:
    print(f'ID: {self.id}\nCapacity: {self.capacity}\nReserved: {self.reserved[0]} | {self.reserved[1]}\nRead Only: {self.read_only}')