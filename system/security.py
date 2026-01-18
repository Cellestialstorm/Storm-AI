DANGEROUS_KEYWORDS = [
    "delete",
    "remove",
    "erase",
    "shutdown",
    "restart",
    "format",
    "kill",
    "terminate",
]

def is_dangerous(command: dict) -> bool:
    command["action"] = command.lower()
    return (any(word in command for word in DANGEROUS_KEYWORDS))