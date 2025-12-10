import pytest

# @pytest.fixture
# def login():
#     print("执行登录操作")
#     return "token_123456"

# def test_order(login):
#     print("下订单，使用", login)

# def test_userinfo(login):
#     print("获取用户信息，使用", login)

# @pytest.fixture
# def a():
#     print("A")
#     return 1

# @pytest.fixture
# def b(a):
#     print("B")
#     return a + 1

# def test_demo(b):
#     print("C")


# @pytest.fixture(scope="session")
# def x():
#     print("X")
#     return 10

# def test_1(x):
#     print(x + 1)

# def test_2(x):
#     print(x + 2)


# fixture函数(类中) 作为多个参数传入
@pytest.fixture()
def login():
    print("打开浏览器")
    a = "account"
    return a
    
@pytest.fixture()
def logout():
    print("关闭浏览器")
 
class TestLogin:
    #传入lonin fixture
    def test_001(self,login):
        print("001传入了loging fixture")
        assert login == "account"
 
    #传入logout fixture
    def test_002(self, logout):
        print("002传入了logout fixture")
 
    def test_003(self, login,logout):
        print("003传入了两个fixture")
 
    def test_004(self):
        print("004未传入仍何fixture哦")
 
if __name__ == '__main__':
        pytest.main()


