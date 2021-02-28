# by Kami Bigdely
# Replace nested conditional with gaurd clauses
import pytest

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)


@pytest.fixture
def test_extract_position():
    '''Returns an empty instance of extract position'''
    return pos == 0

def test_extract_position_2():
    '''Return if bug is in line'''
    line = 'debug'
    assert extract_position(line) == None