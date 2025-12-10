import pytest
# 笛卡尔积，组合数据
# data_1 = [1, 2, 3]
# data_2 = ['a', 'b']
# @pytest.mark.parametrize('a', data_1)
# @pytest.mark.parametrize('b', data_2)
# def test_parametrize_1(a, b):
#     print(f'笛卡尔积 测试数据为 : {a},{b}')
 
 # 标记参数化
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6 * 9", 3, marks=pytest.mark.xfail),
    pytest.param("6*6", 42, marks=pytest.mark.skip)
])
def test_mark(test_input, expected):
    assert eval(test_input) == expected