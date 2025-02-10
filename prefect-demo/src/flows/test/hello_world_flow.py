"""Quick start."""

from prefect import flow


@flow(log_prints=True)
def hello_world_flow(name: str = "world", goodbye: bool = False) -> None:
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":

    """
    Run flow directly, just like Python functions. And the process can also be monitored on UI.
    """
    # hello_world_flow()
    # hello_world_flow(name="Ted", goodbye=True)

    """
    Start a temporary local server of worker to execute flows submitted from Prefect cloud.
    It comes with a development named "my-first-deployment" which can be found on UI.
    """
    # hello_world_flow.serve(
    #     name="my-second-deployment",  # Deployment name. It create a temporary deployment.
    #     tags=["onboarding", "tir104"],  # Filtering when searching on UI.
    #     parameters={
    #         "name": "Allen",
    #         "goodbye": True
    #     },  # Overwrite default parameters defined on hello_world_flow. Only for this deployment.
    #     interval=120,  # Like crontab, "* * * * *"
    # )

    """
    Deploy a flow to Prefect cloud.
    """
    from prefect_github import GitHubRepository
    hello_world_flow.from_source(
        source=GitHubRepository.load("github-repository-uuboyscy"),
        entrypoint="src/flows/test/hello_world_flow.py:hello_world_flow",
    ).deploy(
        name="main",  # Deployment name.
        tags=["dev", "sample"],
        work_pool_name="dev-subproc",  # A worker to submit the deployment.
        parameters=dict(
            name="Marvin"
        ),  # Overwrite default parameters defined on hello_world_flow. Only for this deployment.
        cron="*/15 * * * *",  # Crontab for this deployment.
    )
