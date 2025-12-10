import pytest
class TestExample:
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_network_request(self):
        """网络请求测试,失败重试2次"""
        # 模拟网络请求代码
        assert make_network_request() == "success"
    
    def test_normal_case(self):
        """普通测试，不需要重试"""
        assert 1 + 1 == 2
 
if __name__ == "__main__":
    # 执行所有测试，失败重试1次
    pytest.main(['-v', '--reruns=1', 'test_example.py'])