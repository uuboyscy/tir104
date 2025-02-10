from flows.test.hello_world_flow import hello_world_flow


if __name__ == "__main__":
    from prefect_github import GitHubRepository

    hello_world_flow.from_source(
        source=GitHubRepository.load("github-repository-uuboyscy"),
        entrypoint="src/flow/test/hello_world_flow_flow.py:hello_world_flow",
    ).deploy(
        name="test-deploy",
        tags=["test", "project_1"],
        work_pool_name="test-subproc",
        job_variables=dict(pull_policy="Never"),
        # parameters=dict(name="Marvin"),
        cron="1 * * * *"
    )
