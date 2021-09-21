# Pytests
Rozne sposoby wykonywania testow w pythonie.

Więcej o pytestach: [Pytests.org](https://docs.pytest.org/en/6.2.x/index.html)
* Testy parametryzowane: [Parametrizing tests](https://docs.pytest.org/en/6.2.x/example/parametrize.html#paramexamples)
* Fixture i testy parametryzowane: [Parametrizing fixtures and test functions](https://docs.pytest.org/en/6.2.x/parametrize.html#parametrize-basics)
<br>

Przykład testu sparametryzowanego:
---

```python
@pytest.mark.parametrize: parametrizing test functions

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    
    
```    
## <b>Indirect parametrization</b>

* EN: Using the **indirect=True** parameter when parametrizing a test allows to parametrize a test with a fixture receiving the values before passing them to a test:

* PL: Użycie parametru **indirect=True** podczas parametryzacji testu pozwala na parametryzację testu z uchwytem odbierającym wartości przed przekazaniem ich do testu:

Przykład testu parametryzacja pośrednia:
---

```python
@pytest.fixture
def fixt(request):
    return request.param * 3


@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert len(fixt) == 3
