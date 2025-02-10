from prefect_github import GitHubRepository

from flows.f_02_async_task_flow import f_02_async_task_flow


f_02_async_task_flow.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flow/f_02_async_task_flow.py:f_02_async_task_flow",
).deploy(
    name="test-deploy",
    tags=["test", "project_2"],
    work_pool_name="test-docker",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/5 * * * *"
)
