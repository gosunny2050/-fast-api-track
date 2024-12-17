def to_snake_case(name: str) -> str:
    return ''.join(['_' + i.lower() if i.isupper() else i for i in name]).lstrip('_')

