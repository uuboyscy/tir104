from prefect_github import GitHubRepository

from flows.f_01_quick_start_flow import f_01_quick_start_flow


f_01_quick_start_flow.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flow/f_01_quick_start_flow.py:f_01_quick_start_flow",
).deploy(
    name="test-deploy",
    tags=["test", "project_1"],
    work_pool_name="test-docker",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="1 * * * *"
)
