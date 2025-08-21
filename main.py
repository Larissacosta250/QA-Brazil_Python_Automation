import data
import helpers

URBAN_ROUTES_URL = "https://cnt-bcc03da8-0efe-4621-8304-d98c2c8480bd.containerhub.tripleten-services.com?lng=pt"  # ajuste para a URL real


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes")

    def test_set_route(self):
        print("Função para definir a rota criada com sucesso")
        # Adicionar em S8
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para definir a seleção de plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para teste do número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para o cartão de preenchimento de teste")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para comentário de teste para motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para teste de encomenda de cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Adicionar em S8
            print("Função criada para teste de pedido de 2 sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função modelo de busca de carro de teste aparece")
        pass
