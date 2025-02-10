from prefect_github import GitHubRepository

from flows.f_04_forloop_submit_flow import f_04_forloop_submit_flow


f_04_forloop_submit_flow.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flow/f_04_forloop_submit_flow.py:f_04_forloop_submit_flow",
).deploy(
    name="test-deploy",
    tags=["test", "project_4"],
    work_pool_name="test-docker",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/30 0-8,9-15,16-23 * * *"
)
