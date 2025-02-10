import pandas as pd
from prefect import flow, task

from utils.prefect_utility import generate_flow_name


@task
def e_data_source_1() -> pd.DataFrame:
    print("Getting df1.")
    return pd.DataFrame(data=[[1], [2]], columns=["col"])

@task
def e_data_source_2() -> pd.DataFrame:
    print("Getting df2.")
    return pd.DataFrame(data=[[3], [4]], columns=["col"])

@task
def t_concat(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    print("Concating df1 and df2.")
    return pd.concat([df1, df2]).reset_index(drop=True)

@task
def l_db1(df: pd.DataFrame) -> None:
    print("Loading df to db1.")
    print(df)
    print("===============")

@task
def l_db2(df: pd.DataFrame) -> None:
    print("Loading df to db2.")
    print(df)
    print("===============")

@flow(name=generate_flow_name())
def f_01_quick_start_flow() -> None:
    df1 = e_data_source_1()
    df2 = e_data_source_2()
    df = t_concat(df1, df2)
    l_db1(df)
    l_db2(df)

if __name__ == "__main__":
    # f_01_quick_start_flow()
    from prefect_github import GitHubRepository

    f_01_quick_start_flow()

    # f_01_quick_start_flow.from_source(
    #     source=GitHubRepository.load("github-prefect-demo"),
    #     entrypoint="src/flow/f_01_quick_start_flow.py:f_01_quick_start_flow",
    # ).deploy(
    #     name="test-deploy",
    #     tags=["test", "project_1"],
    #     work_pool_name="test-docker",
    #     job_variables=dict(pull_policy="Never"),
    #     # parameters=dict(name="Marvin"),
    #     cron="1 * * * *"
    # )
