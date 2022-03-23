class C8Memory:
  def __init__(self) -> None:
    self.capacity = 0xFFF
    self.reserved = [0x000, 0x1FF]
    self.start = 0x200
    self.RAM = []
    for i in range(self.capacity):
      self.RAM.append(0)

  def clear_memory(self, clear_reserved: bool = True) -> None:
    if clear_reserved:
      for index in range(self.capacity):
        self.RAM[index] = 0
      return
    else:
      for index in range(self.reserved[1]+1, self.capacity):
        self.RAM[index] = 0