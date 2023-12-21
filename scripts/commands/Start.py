import scripts.commands.execute as execute

class Start():
    def execute(self, option_out):
        execute.command("docker-compose start")
        input("pressione qualquer tecla para continuar...\n")
        return option_out