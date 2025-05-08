import lab2 as lab

def test_find_min_max():
    input_arr = [2,3,4,5,1.2,5.6,2.11,69.1,-0.2]
    result = lab.find_min_max(input_arr)
    target = [min(input_arr), max(input_arr)]
    assert(result == target)
def test_calc_average():
    input_arr = [1,2,3,4]
    result = lab.calc_average(input_arr)
    assert(result == 2.5)
def test_calc_median_temperature():
    input_arr = [3,4,2,1]
    result = lab.calc_median_temperature(input_arr)
    assert(result == 2.5)