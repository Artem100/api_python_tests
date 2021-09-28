class Json(object):
    @staticmethod
    def create_user(name, job):
        json = {
                    "name": name,
                    "job": job
                }
        return json

    @staticmethod
    def view_single_user_json(id: int, email: str, first_name: str, last_name: str, avatar: str, support_url: str,
                              text: str):
        json = {
                "data": {
                    "id": id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "avatar": avatar
                },
                "support": {
                    "url": support_url,
                    "text": text
                }
            }
        return json