from prefect_github import GitHubRepository

from flows.f_03_map_flow import f_03_map_flow


f_03_map_flow.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flow/f_03_map_flow.py:f_03_map_flow",
).deploy(
    name="test-deploy",
    tags=["test", "project_3"],
    work_pool_name="test-docker",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/10 * * * *"
)
