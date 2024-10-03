def test_function():
    def inner_function():
        print("i'm in test_function scope")
    inner_function()

test_function()
#inner_function() NameError: name 'inner_function' is not defined.