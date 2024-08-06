import threading

class ServiceRegistrator:
    services = []

    @classmethod
    def register_service(cls, router):
        cls.services.append(router)

    @classmethod
    def setup_services(cls):
        for service in cls.services:
            threading.Thread(target=eval(f'f{service}().start_service')).start()
