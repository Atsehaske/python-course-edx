import pytest
from seasons import seasons

def test_format():
    with pytest.raises(SystemExit):
        assert seasons('02-02-2000')
        assert seasons('1999:02:01')
        assert seasons('2000/32/02')

