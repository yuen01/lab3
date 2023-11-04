from price_info import total_cost_shopping,cost_of_fruits


def test_total_cost_shopping():
    assert total_cost_shopping() == 46.75


def test_cost_of_fruit():
    assert cost_of_fruits('apple', 5) == 6.0


if __name__ == "__main__":
    test_total_cost_shopping()
