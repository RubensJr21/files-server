import scripts.commands.execute as execute

class Backup():
    def execute(self, option_out):
        execute.command("docker-compose exec -u www-data nextcloud php occ backup:point:create -vvv")
        if((input("deseja desligar o computador? (Y/n) ") in ["Y", "y"])):
            execute.command("shutdown now -p")
            return -1
        else:
            input("pressione qualquer tecla para continuar...\n")
        return option_out