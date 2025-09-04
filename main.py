import data
import helper


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes ")
        else:
            print("Não foi possivel conectar ao Urban Routes.Verifique se o servidor está ligado e ainda em execu

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_from_location_value() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        assert routes_page.click_comfort_active()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.clicl_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in routes_page.numero_confirmado()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()



    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()



    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL
        routes_page = UrbanRoutesPages(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()



    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN
