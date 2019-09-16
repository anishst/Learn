from os import listdir,chdir
import inspect


default_path = r'C:\Users\532975\Documents\Automation\SeleniumPythonFramework\tests\Stability'
modules = [ fl for fl in listdir(default_path) if fl.endswith('.py') ]



class Test(object):
	"""docstring for Test"""
	def test_method():
		"""Test method doc"""

	def test_method2():
		"""Test method 2"""

print(inspect.getdoc(Test))
print(inspect.getsource(Test))

print(inspect.getmembers(Test))
			

print(dir(Test))
print("".center(100, '*'))
print(Test.__dict__.items())
print("".center(100, '*'))
print(Test.__name__)