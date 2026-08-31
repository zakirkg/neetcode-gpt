import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maximum = np.max(z)
        z = z - maximum
        
        exponential = np.exp(z)
        array_sum = sum(exponential)
        return np.round(exponential / array_sum, 4)