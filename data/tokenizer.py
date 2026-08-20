from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        text = [*corpus]

        solution_list = []
        for _ in range(num_merges):
            freq = {}
            for i in range(len(text) - 1):
                pair = text[i] + text[i + 1]

                freq[pair] = freq.get(pair, 0) + 1
            
            if not freq:
                break
            
            merging, _ = min(freq.items(), key=lambda item: (-item[1], len(item[0]), item[0]))

            new_text = []
            i = 0
            
            while i < len(text):
                if (
                    i < len(text) - 1
                    and text[i] + text[i + 1] == merging
                ):
                    new_text.append(merging)
                    sol = [text[i], text[i + 1]]
        
                    if not sol in solution_list:
                        solution_list.append(sol)
                    i += 2
                else:
                    new_text.append(text[i])
                    i += 1
            
            text = new_text
        
        return solution_list