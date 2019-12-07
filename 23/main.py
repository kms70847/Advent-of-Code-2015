import re

def try_ints(seq):
    result = []
    for item in seq:
        try:
            result.append(int(item))
        except:
            result.append(item)
    return result

for part in (1,2):
    program = []
    with open("input") as file:
        for line in file:
            program.append(try_ints(re.split(",? ", line.strip())))

    pc = 0
    registers = {"a": 0 if part == 1 else 1, "b": 0}
    while 0 <= pc < len(program):
        op, *args = program[pc]
        should_advance_pc = True
        if op == "hlf":
            registers[args[0]] //= 2
        elif op == "tpl":
            registers[args[0]] *= 3
        elif op == "inc":
            registers[args[0]] += 1
        elif op == "jmp":
            pc += args[0]
            should_advance_pc = False
        elif op == "jie":
            if registers[args[0]] % 2 == 0:
                pc += args[1]
                should_advance_pc = False
        elif op == "jio":
            if registers[args[0]] == 1:
                pc += args[1]
                should_advance_pc = False
        else:
            raise Exception(f"opcode {op} not implemented yet")
        if should_advance_pc:
            pc += 1
    print(registers["b"])