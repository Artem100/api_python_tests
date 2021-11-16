import allure

from src.api_methods import ApiMethods


class UsersApi(ApiMethods):

    url = f"users/"

    @allure.step
    def getUsersPagesList(self, num_page):
        # User parametr in url ?page={num_page}
        params = {'page': num_page}
        response = self._get_method(self.url, params=params)
        return response

    @allure.step
    def create_new_user(self, body):
        # response = self._post_method(self.url, body, content_type="application/x-www-form-urlencoded; charset=UTF-8")
        response = self._post_method(self.url, body)
        return response

    @allure.step
    def view_single_user(self, id_user):
        response = self._get_method(self.url+id_user)
        return response

