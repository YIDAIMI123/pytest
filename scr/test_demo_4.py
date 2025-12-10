import pytest

@pytest.fixture(params=[(1,2),(3,4)],ids=["a","b"])
def numbers(request):
    return request.param

def test_add(numbers):
    a,b = numbers
    print(a + b)

def test_mul(numbers):
    a,b = numbers
    print(a * b)

# @pytest.mark.parametrize("a,b",[(1,2),(3,4)])
# def test_add(a,b):
#     print(a + b)
if __name__ == '__main__':
    pytest.main()

