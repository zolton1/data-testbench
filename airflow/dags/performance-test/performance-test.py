from airflow import DAG
from datetime import datetime
from airflow.decorators import task
from airflow.models import Variable

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 22),
    "retries": 0,
}

with DAG(
    "performance_test_dag",
    default_args=default_args,
    description="performance_test_dag",
    schedule="*/5 * * * *",
    catchup=False,
    max_active_runs=1,
) as dag:
    
    number_of_tasks = Variable.get("performance_test_number_of_tasks", default_var=5) 

    task_list = [f"task_{x}" for x in list(range(0, number_of_tasks))]

    a = int(len(task_list) * 0.2)

    b = int(len(task_list) * 0.3)

    c = int(len(task_list) * 0.9)

    task_list_a = task_list[:a]

    task_list_b = task_list[a:b]

    task_list_c = task_list[b:c]

    task_list_d = task_list[c:]

    @task
    def pt():
        import hashlib
        import string
        import random

        str_length = Variable.get("performance_test_str_length", default_var=100000)

        m = hashlib.sha256()
        txt = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=str_length)
        )
        m.update(txt.encode("utf-8"))
        print(m.hexdigest())

    def _connect(a_list, b_list, dag=dag):
        for x in a_list:
            for y in b_list:
                dag.get_task(x) >> dag.get_task(y)

    [pt.override(task_id=ti, retries=0)() for ti in task_list]

    _connect(a_list=task_list_a, b_list=task_list_b)

    _connect(a_list=task_list_a, b_list=task_list_c)

    _connect(a_list=task_list_b, b_list=task_list_c)

    _connect(a_list=task_list_b, b_list=task_list_d)

    _connect(a_list=task_list_c, b_list=task_list_d)

