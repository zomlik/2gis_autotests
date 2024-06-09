class TestData:
    INVALID_NAME_REGION = ["FDHF", "Земля", 1235, "@^$%&^&.12"]
    INVALID_NAME_LEN = ["12", "0", "-1", "МС", "Мс"]
    VALID_COUNTRY_CODE = ["ru", "kg", "kz", "cz"]
    INVALID_COUNTRY_CODE = ["ua", 10, " "]
    INVALID_PAGE_SEQUNCE = ["text", 2.10, "@#%."]
    VALID_PAGE_SIZE = [5, 10, 15]
    INVALID_PAGE_SIZE = [-1, 0, 4, 6, 9, 11, 14, 16]
    NOT_INT_TYPE_PAGE_SIZE = [" ", "TEXT", "@.$%"]
