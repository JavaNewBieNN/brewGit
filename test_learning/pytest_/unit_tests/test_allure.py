import allure
import pytest



@allure.epic("1.iot-bms, epic level") #"Ning's demo: allure automatic unit_tests framework, epic level Top layer of the project:"
@allure.feature("2.controller level, feature level") #module 功能模块
@allure.story("3.Peak-shaving, story level")  # "specific function 具体功能， story level"
@allure.title("4.charge_power, title/ut level") # description of unit_tests case unit unit_tests level

@pytest.mark.ut
def test_charge_power():
    assert 1==1

@allure.epic("1.iot-bms, epic level")
@allure.feature("2.controller level, feature level")
@allure.story("3.Peak-shaving, story level")
@allure.title("4.discharge_power, title/ut level")


@pytest.mark.ut
@pytest.mark.xfail  # expected to be false
def test_discharge_power():
    assert 1==2


@allure.epic("1.iot-bms, epic level")
@allure.feature("2.controller level, feature level")
@allure.story("3.state machine, story level")
def test_state():
    assert 1==1

@allure.epic("1.iot-bms, epic level")
@allure.feature("2.controller level, feature level")
@allure.story("3.OTA, story level")
@allure.title("4.get_current_version, title/ut level")
def test_get_current_version():
    assert 1==1