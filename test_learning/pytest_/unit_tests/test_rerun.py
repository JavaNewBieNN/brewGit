import random
import pytest


@pytest.mark.ut
def test_rerun():
    x = random.randint(0, 9)  # 每次都有随机数出现 generate a random int
    assert x >= 5




