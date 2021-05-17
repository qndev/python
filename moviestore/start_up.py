from moviestore.app.program import Program


class StartUp:

    def run(self, root_dir: str):
        Program().execute(root_dir)
