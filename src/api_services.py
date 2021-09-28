from src.api_methods import ApiMethods


class UsersApi(ApiMethods):
    url = f"users"
    def getUsersPagesList(self, num_page: str):
        # User parametr in url ?page={num_page}
        # url = f"api/users?page={num_page}"
        params = {'page': num_page}
        response = self._get_method(self.url, content_type="application/x-www-form-urlencoded; charset=UTF-8", params=params)
        return response

    def create_new_user(self, body):
        # response = self._post_method(self.url, body, content_type="application/x-www-form-urlencoded; charset=UTF-8")
        response = self._post_method(self.url, body)
        return response
