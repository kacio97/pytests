# pytests
Rozne sposoby wykonywania testow

<b>@pytest.mark.parametrize: parametrizing test functions</b>

<i>@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])</i><br>
def test_eval(test_input, expected):<br>
    assert eval(test_input) == expected<br>
    
    =======================
    
<b>Indirect parametrization</b>

Using the indirect=True parameter when parametrizing a test allows to parametrize a test with a fixture receiving the values before passing them to a test:

<i>@pytest.fixture</i><br>
def fixt(request):<br>
    return request.param * 3<br>


<i>@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)</i><br>
def test_indirect(fixt):<br>
    assert len(fixt) == 3<br>
