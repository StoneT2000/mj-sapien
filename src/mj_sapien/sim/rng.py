import numpy as np

from mj_sapien.types import TensorLike


class BatchedRNG:
    def __init__(self, seed: int | None = None):
        self.rng = np.random.default_rng(seed)

    def rand(self, shape: tuple[int, ...]) -> TensorLike:
        return self.rng.random(shape)

    def randint(self, low: int, high: int, shape: tuple[int, ...]) -> TensorLike:
        return self.rng.integers(low, high, shape)

    def randn(self, shape: tuple[int, ...]) -> TensorLike:
        return self.rng.normal(shape)
