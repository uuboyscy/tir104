import pandas as pd
from prefect import flow, task

from utils.prefect_utility import generate_flow_name


@task
def generate_some_str() -> str:
    return "HELLO"

@task
def do_something(some_str: str) -> list[str]:
    return list(some_str)

@task
def print_something_separately(something: str | list) -> None:
    print("======")
    print(something)
    print("======")

@flow(name=generate_flow_name())
def f_04_forloop_submit_flow() -> None:
    some_str = generate_some_str()
    result = do_something(some_str)
    for each_str in result:
        print_something_separately.submit(each_str)

if __name__ == "__main__":
    from prefect_github import GitHubRepository
    f_04_forloop_submit_flow()

    # f_04_forloop_submit_flow.from_source(
    #     source=GitHubRepository.load("github-prefect-demo"),
    #     entrypoint="src/flow/f_04_forloop_submit_flow.py:f_04_forloop_submit_flow",
    # ).deploy(
    #     name="test-deploy",
    #     tags=["test", "project_4"],
    #     work_pool_name="test-docker",
    #     job_variables=dict(pull_policy="Never"),
    #     # parameters=dict(name="Marvin"),
    #     cron="*/30 0-8,9-15,16-23 * * *"
    # )
