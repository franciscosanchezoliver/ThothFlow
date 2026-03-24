class RepoTask:

    def __init__(
        self,
        repo_url,
        entry_point,
        input_spec,
        output_spec
    ):
        self.repo_url = repo_url
        self.entry_point = entry_point
        self.input_spec = input_spec
        self.output_spec = output_spec

    def run(self, input):
        # 1. Clone / Pull Repository

        # 2. Execute Entry Point (could be a simple script or a complex system)

        # 3. Return an output

        pass
