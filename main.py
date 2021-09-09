# from calculator.calculate import Calculate
import os

import calc_module
import pytest


# @pytest.mark.parametrize("input_d, expected",
#                          [("3+5*2", ["+", "*"]), ("6-2+5*2", ["-", "+", "*"]), ("12*2+14-10", ["*", "+", "-"])])
# def test_correct_parsed_signs(input_d, expected):
#     signs = Calculate(input_d)
#     signs.parse_equaliton()
#     assert signs.signs == expected
#
#
# @pytest.mark.parametrize("test_input, expected",
#                          [("3+5*2", [3, 5, 2]), ("6-2+5*2", [6, 2, 5, 2]), ("12*2+14-10", [12, 2, 14, 10])])
# def test_correct_parsed_values(test_input, expected):
#     cal = Calculate(test_input)
#     cal.parse_equaliton()
#     assert cal.values == expected
#
#
# @pytest.fixture()
# def equalition_data_five_signs():
#     cal = Calculate("3+2*4-2*5/2")
#     return cal
#
#
# @pytest.fixture(params=["3+5*2", "6-2+5*2", "12*2+14-10"])
# def prepare_data_for_equalition(request):
#     calc = Calculate(request.param)
#     calc.parse_equaliton()
#     print("start preparation !")
#     yield calc
#     print("finish preparation !")
#
#
# def test_carry_out_equalition(prepare_data_for_equalition):
#     c = prepare_data_for_equalition.equalition
#     assert c == 13 or c == 14 or c or c == 28
#
#
# def test_correct_parsed(equalition_data_five_signs):
#     expected_values = [3.0, 2.0, 4.0, 2.0, 5.0, 2.0]
#     expected_signs = ["+", "*", "-", "*", "/"]
#     cal = equalition_data_five_signs
#     cal.parse_equaliton()
#     values = cal.values
#     signs = cal.signs
#     for i in range(len(values)):
#         assert values[i] == expected_values[i]
#     assert expected_signs == signs


# calculate_from_file("data.txt")
#
#
# @pytest.mark.parametrize("file_name, input_eq, expected", [("easy_eq.txt", "1+2+3 5*5+1 2*4+5", [6.0, 26.0, 13.0]),
#                                                            ("hard_eq.txt", "1*5+10*2-6/2 4/2-1+5*5-5 12+13*2+2*18/2",
#                                                             [22.0, 21.0, 56.0])])
# def test_calc_module(file_name, input_eq, expected):
#     if ".txt" in str(file_name):
#         with open(file_name, "w") as f:
#             f.write(input_eq)
#
#     results = calc_module.calculate_from_file(file_name)
#     assert results == expected
#     f.close()
# =======================================================================#
# SOLUTION: 1

# @pytest.fixture(params=["eq.txt"])
# def mock_data(request):
#     filename = request.param
#     if ".txt" in str(filename):
#         with open(filename, "w") as f:
#             f.write("1+2+3 5*5+1 2*4+5 1*5+10*2-6/2\n4/2-1+5*5-5 12+13*2+2*18/2")
#     yield filename
#     f.close()
#
#
# @pytest.mark.parametrize("expected", [([6.0, 26.0, 13.0, 22.0, 21.0, 56.0])])
# def test_calc_module(mock_data, expected):
#     results = calc_module.calculate_from_file(mock_data)
#     assert results == expected

# SOLUTION 2

# @pytest.fixture(params=[pytest.param(("eq.txt", "1+2+3 2+2", [6, 4])), pytest.param(("eq_2.txt", "1+2 2-2", [3, 0]))])
# def mock_data(request):
#     filename = request.param[0]
#     if ".txt" in str(filename):
#         with open(filename, "w") as f:
#             f.write(request.param[1])
#             print("SetUp()")
#     yield [filename, request.param[2]]
#     f.close()
#     os.remove(filename)
#     print("TearDown()")
#
#
# def test_calc_module(mock_data):
#     results = calc_module.calculate_from_file(mock_data[0])
#     if results:
#         assert results == mock_data[1]
#     else:
#         assert results == 0
#         print("Exit with 0 no equalition")
# =======================================================================#

# INDIRECT PARAMETRIZATION
# @pytest.fixture
# def fixt(request):
#     return request.param * 3
#
#
# @pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
# def test_indirect(fixt):
#     assert len(fixt) == 3

@pytest.fixture
def mock_data(request):
    filename = "file.txt"
    if ".txt" in str(filename):
        with open(filename, "w") as f:
            f.write(request.param[0])

    yield [filename, request.param[1]]
    f.close()


@pytest.mark.parametrize("mock_data",
                         [("1+2+3", 6.0), ("5*5+1", 26.0), ("2*4+5", 13.0)],
                         indirect=True)
def test_calc_module(mock_data):
    results = calc_module.calculate_from_file(mock_data[0])

    assert results[0] == mock_data[1]
