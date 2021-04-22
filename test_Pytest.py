import pytest

class Test_Pytest():

    def setup(self):
        print("setup方法执行")

    def teardown(self):
        print("teardown方法执行")

    def test_ll(self):
        print("test_ll")
        assert 1==1

    def test_kk(self):
        print("test_kk")
        assert "o" in "love"

    def test_tt(self):
        print("test_tt")
        assert 3-2==1

if __name__=="__main__":
    pytest.main(['-v','test_Pytest.py'])
