from lab2.bmi import calculate_bmi

def test_bmi_normal_weight():
    height = 1.73
    weight = 57
    bmi = calculate_bmi(height, weight)
    bmicheck = 0
    assert bmi == bmicheck

def test_bmi_under_weight():
    height = 1.73
    weight = 5
    bmi = calculate_bmi(height, weight)
    bmicheck = -1
    assert bmi == bmicheck

def test_bmi_over_weight():
    height = 1.73
    weight = 157
    bmi = calculate_bmi(height, weight)
    bmicheck = 1
    assert bmi == bmicheck