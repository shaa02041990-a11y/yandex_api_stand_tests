import sender_stand_request
from data import (
    kit_body_1, kit_body_2, kit_body_3, kit_body_4, kit_body_5, kit_body_6, kit_body_7, kit_body_8, kit_body_9, kit_body_10, kit_body_11
)
def get_token ():
    return
sender_stand_request.get_new_user_token()
def positive_assert (kit_body):
    token = get_token()
    response = sender_stand_request.post_new_kit(kit_body, token)
    assert response.status_code == 201
def negative_assert(kit_body):
    token = get_token()
    response = sender_stand_request.post_new_kit(kit_body, token)
    assert response.status_code == 400
def test_1_name_one_symbol():
    positive_assert(kit_body_1)
def test_2_name_511_symbols():
    positive_assert(kit_body_2)
def test_3_empty_string():
    negative_assert(kit_body_3)
def test_4_name_512_symbol():
    negative_assert(kit_body_4)
def test_5_english_letters():
    positive_assert(kit_body_5)
def test_6_russian_letters():
    positive_assert(kit_body_6)
def test_7_special_symbols():
    positive_assert(kit_body_7)
def test_8_spaces():
    positive_assert(kit_body_8)
def test_9_digits():
    positive_assert(kit_body_9)
def test_10_no_name_parameter():
    negative_assert(kit_body_10)
def test_11_name_no_string():
    negative_assert(kit_body_11)