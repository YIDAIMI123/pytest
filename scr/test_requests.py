import requests
import pytest
import jsonpath
user_info = {
    "username": "admin",
    "password": "123456"
}
@pytest.mark.skip
def test_github_api():
    r = requests.get("https://api.github.com")
    print(r.status_code)
    assert r.status_code == 200
@pytest.mark.skip
def test_requests():
    r = requests.request(
        method="get",
        url="https://api.github.com",
        data=user_info, #如果data参数是一个字典，则自动将其识别为表单，并自动添加请求头header(只有在request才能用),就是content-type的值是表单类型，json和file也是同理，就不需要在headers中定义content-type了
    )
    assert r.status_code == 200

params = {
    "name": "tom",
    "age": 18
}

def test_get():
    r = requests.request(
        method="get",
        url="https://httpbin.org/get",
        data=params
    )
    print(r.text)
    print(r.status_code)
    print(r.url)

    # token_1 = jsonpath.jsonpath(r.json(), "$.token")[0]
    # print(token_1)

    assert r.status_code == 200

    