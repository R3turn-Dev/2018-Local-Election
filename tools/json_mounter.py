class JsonMounter:
    def __repr__(self):
        return repr(self.__dict__)

    def __init__(self, template: dict):
        for k, v in template.items():
            if isinstance(v, dict):
                template[k] = JsonMounter(v)

            if isinstance(v, list):
                for idx in range(len(v)):
                    if isinstance(template[k][idx], dict):
                        template[k][idx] = JsonMounter(template[k][idx])

        self.__dict__ = template
