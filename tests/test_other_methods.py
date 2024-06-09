from api.routes import Routes


# ТС-21 Запрос с методом HEAD
def test_check_method_head(regions):
    regions.head(Routes.GET_REGIONS)
    regions.status_code_is(200)


# ТС-22.1 Запрос с недоступным методом POST
def test_not_allowed_method_post(regions):
    regions.post(Routes.GET_REGIONS)
    regions.status_code_is(405)


# ТС-22.2 Запрос с недоступным методом PUT
def test_not_allowed_method_put(regions):
    regions.put(Routes.GET_REGIONS)
    regions.status_code_is(405)


# ТС-22.3 Запрос с недоступным методом PATCH
def test_not_allowed_method_path(regions):
    regions.patch(Routes.GET_REGIONS)
    regions.status_code_is(405)


# ТС-22.4 Запрос с недоступным методом DELETE
def test_not_allowed_method_delete(regions):
    regions.delete(Routes.GET_REGIONS)
    regions.status_code_is(405)


# ТС-22.5 Запрос с недоступным методом OPTIONS
def test_not_allowed_method_options(regions):
    regions.options(Routes.GET_REGIONS)
    regions.status_code_is(405)
