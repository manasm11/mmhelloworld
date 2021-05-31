from mmhelloworld import say_hello


def test_say_hello_no_params():
    assert say_hello() == "Hello! World"


def test_say_hello_with_param():
    assert say_hello("Everyone") == "Hello! Everyone"
