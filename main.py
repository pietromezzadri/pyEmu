from memory.c8_memory import C8Memory
from editor.chip_editor import ChipEditor

mem  =  C8Memory()

mem.clear_memory(False)

mem.RAM = [1]*mem.capacity

print(f'size: {len(mem.RAM)}')

mem.clear_memory()

mem.display_info()
print(mem.RAM[511])
print(mem.RAM[512])
