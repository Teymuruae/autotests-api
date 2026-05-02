import random

import pytest
PLATFORM = 'Windows'

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition = PLATFORM == 'Macos')
class TestRerun:

    def test_1(self):
        assert random.choice((True, False))