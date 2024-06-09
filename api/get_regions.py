from api.api import ApiClient
from api.routes import Routes


class GetRegions(ApiClient):
    def get_regions(self):
        return self.get(Routes.GET_REGIONS)

    def get_regions_by_query_q(self, value):
        return self.get(Routes.GET_REGIONS, query={"q": value})

    def get_regions_by_query_country_code(self, country_code):
        return self.get(Routes.GET_REGIONS, query={"country_code": country_code})

    def get_regions_by_query_page(self, page):
        return self.get(Routes.GET_REGIONS, query={"page": page})

    def get_regions_by_query_page_size(self, page_size):
        return self.get(Routes.GET_REGIONS, query={"page_size": page_size})

    def get_regions_all_query(self, q, country_code, page_size, page):
        return self.get(Routes.GET_REGIONS, query={"q": q,
                                                   "country_code": country_code,
                                                   "page_size": page_size,
                                                   "page": page,
                                                   })

    def json_all_items(self):
        return self.get_json()["items"]

    def json_item_name_by_id(self, id_item: int):
        return self.get_json()["items"][id_item]["name"]

    def json_error_message(self):
        return self.get_json()["error"]["message"]

    def len_elements_in_items(self):
        return len(self.get_json()["items"])
