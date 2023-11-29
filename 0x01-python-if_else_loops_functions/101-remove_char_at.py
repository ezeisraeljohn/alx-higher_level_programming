#!/usr/bin/python3
def remove_char_at(input_str: str, index: int) -> str:
    if 0 <= index < len(input_str):
        updated_str = ''.join(char for i, char in enumerate(input_str)
                              if i != index)
        return updated_str
    else:
        return input_str
