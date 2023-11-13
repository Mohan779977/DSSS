def test_division_positive():
    # Given
    num1 = 10
    num2 = 5

    # When
    actual_result = division(num1, num2)

    # Then
    assert actual_result == 2


def test_division_negative():
    # Given
    num1 = -10
    num2 = 5

    # When
    actual_result = division(num1, num2)

    # Then
    assert actual_result == -2


def test_division_by_zero():
    # Given
    num1 = 10
    num2 = 0

    # When
    try:
        actual_result = division(num1, num2)
    except ValueError as e:
        # Then
        assert str(e) == "division by zero"
    else:
        assert False, "Expected ValueError but no exception was raised"
