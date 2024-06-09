import pytest
from test_data.regions_data import TestData


# TC-1 Получение регионов без query параметров
def test_get_regions_default(regions):
    regions.get_regions()
    regions.status_code_is(200)
    regions.json_shema_is_valid()


# TC-2 Фильтрация региона по частичному совпадению поля name 3 символов
def test_filter_min_value_q(regions):
    regions.get_regions_by_query_q("мос")
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.json_item_name_by_id(0) == "Москва"


# ТС-3 Фильтрация региона по максимальному значению q
def test_filter_max_value_q(regions):
    regions.get_regions_by_query_q("а" * 30)
    regions.status_code_is(200)
    regions.json_shema_is_valid()


# ТС-4 Фильтрация региона с превышением максимального значения q=30 символов
def test_exceed_max_value_q(regions):
    regions.get_regions_by_query_q("б" * 31)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'q' должен быть не более 30 символов"


# TC-5 Фильтрация региона по полному совпадению поля name
def test_full_name_filter(regions):
    regions.get_regions_by_query_q("Новосибирск")
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.json_item_name_by_id(0) == "Новосибирск"


# TC-6 Фильтрация региона поле name в верхнем регистре
def test_filter_up_register(regions):
    regions.get_regions_by_query_q("МОСКВА")
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.json_item_name_by_id(0) == "Москва"


# TC-7 Фильтрация региона по не существующему полю name
@pytest.mark.parametrize("name_data", TestData.INVALID_NAME_REGION)
def test_filter_name_not_exist(regions, name_data):
    regions.get_regions_by_query_q(name_data)
    regions.json_shema_is_valid()
    assert regions.json_all_items() == []


# TC-8 Получение списка регионов на странице по умолчанию
def test_get_regions_quantity_default(regions):
    regions.get_regions()
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.len_elements_in_items() == 15


# TC-9 Фильтрация регионов по полю name длинной 2 символа
@pytest.mark.parametrize("name_data", TestData.INVALID_NAME_LEN)
def test_filter_2_sibbols(regions, name_data):
    regions.get_regions_by_query_q(name_data)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'q' должен быть не менее 3 символов"


# ТС-10 Фильтрация регионов с параметрами q, country_code, page_size, page
def test_all_query_params(regions):
    regions.get_regions_all_query(q="Москва", country_code="ua", page_size=5, page=3)
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.json_item_name_by_id(0) == "Москва"


# ТС-11 Фильтрация регионов по коду страны
@pytest.mark.parametrize("data_code", TestData.VALID_COUNTRY_CODE)
def test_valid_code_country(regions, data_code):
    regions.get_regions_by_query_country_code(data_code)
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    json = regions.get_json()
    for j in json["items"]:
        assert j["country"]["code"] == data_code


# ТС-12 Фильтрация регионов по невалидному коду страны
@pytest.mark.parametrize("data_code", TestData.INVALID_COUNTRY_CODE)
def test_invalid_country_code(regions, data_code):
    regions.get_regions_by_query_country_code(data_code)
    regions.status_code_is(200)
    assert regions.json_error_message() == ("Параметр 'country_code' может быть"
                                            " одним из следующих значений: ru, kg, kz, cz")


# ТС-13 Порядковый номер страницы
def test_page_sequence_number_2(regions):
    regions.get_regions_by_query_page(2)
    regions.status_code_is(200)
    regions.json_shema_is_valid()


# ТС-14 Получение списка регионов с нулевым порядковым номером страницы
def test_page_null_sequence_number(regions):
    regions.get_regions_by_query_page(0)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'page' должен быть больше 0"


# ТС-15 Получение списка регионов с отрицательным порядковым номером страницы
def test_page_negative_sequence_number(regions):
    regions.get_regions_by_query_page(-1)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'page' должен быть больше 0"


# ТС-16 Получение списка регионов с не верным типом значения параметра page
@pytest.mark.parametrize("data_page", TestData.INVALID_PAGE_SEQUNCE)
def test_page_wrong_type_sequnce_number(regions, data_page):
    regions.get_regions_by_query_page(data_page)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'page' длжен быть целым числом"


# ТС-17 Получение списка регионов с порядковым номером страницы
# большее чем количество элементов в БД
def test_page_more_than_in_bd(regions):
    regions.get_regions_by_query_page(15)
    regions.status_code_is(200)
    assert regions.json_all_items() == []


# ТС-18 Количество отображаемых элементов на странице при значении page_size [5, 10, 15]
@pytest.mark.parametrize("data_page_size", TestData.VALID_PAGE_SIZE)
def test_page_size_valid(regions, data_page_size):
    regions.get_regions_by_query_page_size(data_page_size)
    regions.status_code_is(200)
    regions.json_shema_is_valid()
    assert regions.len_elements_in_items() == data_page_size


# ТС-19 Количество отображаемых элементов с не валидным значением page_size
@pytest.mark.parametrize("data_page_size", TestData.INVALID_PAGE_SIZE)
def test_invalid_page_size_params(regions, data_page_size):
    regions.get_regions_by_query_page_size(data_page_size)
    regions.status_code_is(200)
    assert regions.json_error_message() == ("Параметр 'page_size' может быть "
                                            "одним из следующих значений: 5, 10, 15")


# ТС-20 Количество отображаемых элементов со значением page_size type
@pytest.mark.parametrize("data_page_size", TestData.NOT_INT_TYPE_PAGE_SIZE)
def test_invalid_page_size_type(regions, data_page_size):
    regions.get_regions_by_query_page_size(data_page_size)
    regions.status_code_is(200)
    assert regions.json_error_message() == "Параметр 'page_size' длжен быть целым числом"
