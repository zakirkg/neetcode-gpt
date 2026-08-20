from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        temp_var = sorted(list(set([*text])))
        stoi = {char: i for i, char in enumerate(temp_var, start=0)}
        itos = {i: char for char, i in stoi.items()}
        return (stoi, itos)

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        encoded = [stoi[char] for char in text]
        return encoded

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        decoded_chars = [itos[id] for id in ids]
        decoded_string = "".join(decoded_chars)
        return decoded_string
