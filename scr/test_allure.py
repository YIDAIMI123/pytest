import os

import pytest
@pytest.mark.parametrize("a,b,sum",[    #这是定义在测试函数上的，@fixture是定义在普通函数上(不是定义在测试函数上)
    (1,2,3),
    (4,5,9),
    (10,20,10086),
])
def test_add(a,b,sum):
    assert a + b == sum
# 运行pytest测试框架的主函数
if __name__ == '__main__':
    pytest.main()
    # 调用allure生成报告
    # os.system("allure generate ./temp -o ./report --clean")
