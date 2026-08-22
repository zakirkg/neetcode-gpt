from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        tokens = sorted(vocab.keys(), key=lambda s: (len(s), s), reverse=True)

        solution = []
        for num in numbers:
            str_num = str(num)
            temp = []
            i = 0
            while i < len(str_num):
                for token in tokens:
                    if str_num.startswith(token, i):
                        temp.append(token)
                        i += len(token)
                        break
            solution.append(temp)
        return solution



    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        tokens = sorted(vocab.keys(), key=lambda s: len(s), reverse=True)
        i = 0
        
        token_count = 0
        while i < len(text):
            for token in tokens:
                if text.startswith(token, i):
                    token_count += 1
                    i += len(token)
                    break
        return token_count


    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        word_count = len(text.split(" "))

        token_count = self.count_tokens(text, vocab)
        fertility = token_count / word_count

        return round(fertility, 4)
