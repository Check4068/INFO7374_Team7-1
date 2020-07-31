from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def get_ncf(self):
        self.client.get("/ncf/21")

    @task
    def get_npa(self):
        self.client.get("/npa/21")
