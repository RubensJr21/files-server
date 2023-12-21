import scripts.commands.execute as execute

class Restart():
    def execute(self, option_out):
        execute.command("docker-compose restart")
        input("pressione qualquer tecla para continuar...\n")
        return option_out