import scripts.commands.execute as execute

class Ps():
    def execute(self, option_out):
        execute.command("docker-compose ps")
        input("pressione qualquer tecla para continuar...\n")
        return option_out