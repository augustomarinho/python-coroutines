from locust import HttpUser, task, tag, TaskSet, constant_pacing


class TaskCase7(TaskSet):

    @task(1)
    @tag("case7")
    def task_7(self):
        self.client.get("/7/async-io-bound", catch_response=False)


class TaskCase71(TaskSet):

    @task(1)
    @tag("case71")
    def task_7_1(self):
        self.client.get("/7_1/async-io-bound", catch_response=False)


class TaskCase72(TaskSet):

    @task(1)
    @tag("case72")
    def task_7_2(self):
        self.client.get("/7_2/async-io-bound", catch_response=False)


class TaskCase73(TaskSet):

    @task(1)
    @tag("case73")
    def task_7_3(self):
        self.client.get("/7_3/async-io-bound", catch_response=False)


class Case7User(HttpUser):
    wait_time = constant_pacing(0.5)
    network_timeout = 60.0
    connection_timeout = 3.0
    fixed_count = 100
    tasks = [TaskCase7, TaskCase71, TaskCase72, TaskCase73]
