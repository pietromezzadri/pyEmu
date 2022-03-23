from memory.c8_memory import C8Memory

mem  =  C8Memory()

mem.clear_memory(False)

print(len(mem.RAM))
print(mem.RAM)
print(mem.RAM[0x1FF])
print(0x1FF)
