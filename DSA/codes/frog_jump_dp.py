from os import *
from sys import *
from collections import *
from math import *

from typing import *


def frogJump(n: int, h: List[int]) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 0
    dp[2] = abs(h[1] - h[0])

    for i in range(3, n + 1):
        dp[i] = min(dp[i - 2] + abs(h[i - 1] - h[i - 3]),
                    dp[i - 1] + abs(h[i - 1] - h[i - 2])
                    )

    return dp[n]

