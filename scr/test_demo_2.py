import pytest

@pytest.mark.parametrize("a,b,sum",[    #这是定义在测试函数上的，@fixture是定义在fixture上
    (1,2,3),
    (4,5,9),
    (10,20,30),
])
def test_add(a,b,sum):
    assert a + b == sum
