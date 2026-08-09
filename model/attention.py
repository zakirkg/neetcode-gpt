import torch
import torch.nn as nn
from torchtyping import TensorType

class SingleHeadAttention(nn.Module):

    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # Create three linear projections (Key, Query, Value) with bias=False
        # Instantiation order matters for reproducible weights: key, query, value
        self.w_k = nn.Linear(embedding_dim, attention_dim, bias=False) #(embedding_dim, attention_dim)
        self.w_q = nn.Linear(embedding_dim, attention_dim, bias=False) #(embedding_dim, attention_dim)
        self.w_v = nn.Linear(embedding_dim, attention_dim, bias=False) #(embedding_dim, attention_dim)

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # 1. Project input through K, Q, V linear layers
        # 2. Compute attention scores: (Q @ K^T) / sqrt(attention_dim)
        # 3. Apply causal mask: use torch.tril(torch.ones(...)) to build lower-triangular matrix,
        #    then masked_fill positions where mask == 0 with float('-inf')
        # 4. Apply softmax(dim=2) to masked scores
        # 5. Return (scores @ V) rounded to 4 decimal places
        # x = embedded (batch_size, seq_len, embedding_dim)
        Q = self.w_q(embedded) #(batch_size, seq_len, attention_dim)
        K = self.w_k(embedded) #(batch_size, seq_len, attention_dim)
        V = self.w_v(embedded) #(batch_size, seq_len, attention_dim)

        scores = Q @ torch.transpose(K, -1, 1) / math.sqrt(Q.shape[-1]) #(batch_size, seq_len, seq_len)
        mask = torch.tril(torch.ones(Q.shape[1], Q.shape[1]))

        masked_scores = scores.masked_fill(mask == 0, float("-inf"))
        softmax_scores = torch.softmax(masked_scores, dim=2) #(batch_size, seq_len, seq_len)

        outputs = softmax_scores @ V #(batch_size, seq_len, attention_dim)
        return torch.round(outputs, decimals=4)