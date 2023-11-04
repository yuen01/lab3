from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept


def test_get_employees_by_age_range():
    exp_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                  {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
                  {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
                  {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    result = get_employees_by_age_range(22, 33)

    assert (result == exp_result)


def test_calculate_average_salary():
    assert calculate_average_salary() == 60166.666666666664


def test_get_employees_by_dept():
    exp_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                  {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = get_employees_by_dept('Sales')
    assert result == exp_result


if __name__ == "__main__":
    test_get_employees_by_age_range()
    test_calculate_average_salary()
    test_get_employees_by_dept()
