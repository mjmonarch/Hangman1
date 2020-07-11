def what_to_do(instructions):
    simon = "Simon says"
    if instructions.startswith(simon):
        return f"I {instructions[len(simon)+1:]}"
    if instructions.endswith(simon):
        return f"I {instructions[:(len(instructions) - len(simon))]}"
    return "I won't do it!"
