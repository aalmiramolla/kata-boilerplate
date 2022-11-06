from hamcrest import assert_that, equal_to

from app import sample


def test_sum_values():
    """Check if sum function do their job."""
    # Arrange
    first_value = 2
    second_value = 2
    expected_result = 4

    # Action
    current_result = sample.sum(first_value, second_value)

    # Assert
    assert_that(expected_result, equal_to(current_result))
