class Json(object):
    @staticmethod
    def create_user(name, job):
        json = {
                    "name": name,
                    "job": job
                }
        return json