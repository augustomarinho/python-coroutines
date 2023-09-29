from locust import HttpUser, task, between, tag, TaskSet, constant_pacing


class TaskCase6(TaskSet):
    wait_time = constant_pacing(0.5)
    network_timeout = 60.0
    connection_timeout = 3.0
    weight = 3

    @task
    @tag("case6")
    def task_6(self):
        with self.client.get("/6/async-cpu-bound", catch_response=True) as response:
            if response.status_code != 200:
                raise Exception(f"Initial request failed with status code {response.status_code}. Stopping the test.")


class TaskCase61(TaskSet):
    wait_time = constant_pacing(0.5)
    network_timeout = 60.0
    connection_timeout = 3.0
    weight = 3

    @task
    @tag("case61")
    def task_6_1(self):
        with self.client.get("/6_1/async-cpu-bound", catch_response=True) as response:
            if response.status_code != 200:
                raise Exception(f"Initial request failed with status code {response.status_code}. Stopping the test.")


class TaskCase62(TaskSet):
    wait_time = constant_pacing(0.5)
    network_timeout = 60.0
    connection_timeout = 3.0
    weight = 3

    @task
    @tag("case62")
    def task_6_2(self):
        with self.client.get("/6_2/async-cpu-bound", catch_response=True) as response:
            if response.status_code != 200:
                raise Exception(f"Initial request failed with status code {response.status_code}. Stopping the test.")


class TaskCase63(TaskSet):
    wait_time = constant_pacing(0.5)
    network_timeout = 60.0
    connection_timeout = 3.0
    weight = 3

    @task
    @tag("case63")
    def task_6_3(self):
        with self.client.get("/6_3/async-cpu-bound", catch_response=True) as response:
            if response.status_code != 200:
                raise Exception(f"Initial request failed with status code {response.status_code}. Stopping the test.")


class Case6User(HttpUser):
    tasks = [TaskCase6, TaskCase61, TaskCase62, TaskCase63]