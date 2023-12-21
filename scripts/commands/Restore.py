import scripts.commands.execute as execute

class Restore():
    def execute(self, option_out):
        execute.command("docker-compose exec -u www-data nextcloud php occ backup:point:create -vvv")
        if((input("deseja desligar o computador? (Y/n) ") in ["Y", "y"])):
            execute.command("shutdown now -p")
            return -1
        else:
            input("pressione qualquer tecla para continuar...\n")
        return option_out

"""
Forma automatizada de restauração de backup
echo "Executando o comando 'restore'..."
# Coloque aqui o código para o comando 'restore'
# Executa passo a passo para a restauração do backup
$nome_backup=`(docker-compose exec -u www-data nextcloud php occ backup:point:list) | grep -E -o '[0-9]{14}-full-[A-Za-z|0-9]{15}' | head -1`

# Baixa o backup do armazenamento externo
docker-compose exec -u www-data nextcloud php occ backup:point:download $nome_backup --external 1

# Descompacta o backup
docker-compose exec -u www-data nextcloud php occ backup:point:unpack $nome_backup --no-interaction

#Restaura evetivamente
docker-compose exec -u www-data nextcloud php occ backup:point:restore $nome_backup --no-interaction
;;
"""