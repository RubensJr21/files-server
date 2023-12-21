import scripts.commands.execute as execute

"""
docker-compose rm -sv
docker system prune
sudo rm -r ./data-docker/mariaDB/*
sudo rm -r ./data-docker/nextcloud/*
sudo rm -r ./data-docker/onlyoffice/*
sudo rm -r ./data-docker/minIO/*
"""

class Clean():
    def execute(self, option_out):
        execute.command("docker-compose rm -sv")
        execute.command("docker system prune")
        execute.command("sudo rm -r ~/servidor_de_arquivos/data-docker/{nextcloud,mariaDB,onlyoffice,minIO}")
        input("pressione qualquer tecla para continuar...\n")
        return option_out