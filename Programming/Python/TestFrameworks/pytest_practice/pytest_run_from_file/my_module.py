import pytest


def main():
    # pytest.main(['-s', '-v','test_module.py'])
    pytest.main(['-s', '-v', 'test_module.py::TestFooBar'])
    pytest.main(['-s', '-v', 'test_module2.py::TestFooBar'])

if __name__ == '__main__':
    main()