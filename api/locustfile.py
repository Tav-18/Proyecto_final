from locust import HttpUser, task, between

class StressTestUser(HttpUser):
    wait_time = between(1, 5)  # Intervalo entre cada solicitud

    @task
    def load_index(self):
        self.client.get("/")  # Prueba la página de inicio

    @task
    def load_camera(self):
        self.client.get("/camera.html")  # Prueba la página de cámara

    @task
    def interact_modal(self):
        self.client.post("/api/modal", json={"option": "choking"})  # Simula interacción con el modal
