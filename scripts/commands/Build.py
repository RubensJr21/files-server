import time

# Libs Locals
import scripts.commands.execute as execute
import scripts.commands.config as config
import scripts.commands.nextcloud as nextcloud

class Build():
    def execute(self, option_out):
        # return option_out
        execute.command("docker-compose -p \"servidor_de_arquivos\" --env-file .env up -d --remove-orphans")

        inicio = time.time()
        nextcloud.wait_installation()
        fim = time.time()
        tempo_de_execucao = fim - inicio
        print(f"O nextcloud está instalado! (demorou {tempo_de_execucao:.4f} segundos)")

        config.Backup().execute()

        # execute.command("docker-compose exec -u www-data nextcloud php occ user:resetpassword admin")

        config.Theme().execute()

        if((input("deseja ativar o onlyoffice? (Y/n) ") in ["Y", "y"])):
            config.OnlyOffice().execute()
        
        input("pressione qualquer tecla para continuar...\n")

        return option_out


# https://unix.stackexchange.com/questions/418616/python-how-to-print-value-that-comes-from-os-system#:~:text=os.system()%20just%20runs%20the%20process%2C
# https://regex101.com/
# https://www.online-python.com/KXmLvup8J6

# https://www.automate-nova.ro/cloud/core/doc/admin/configuration/server/occ_command.html#files-external-label
# https://docs.openio.io/latest/source/integrations/cookbook_nextcloud.html
# https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/reset_admin_password.html

# https://stackoverflow.com/questions/44060516/multiple-stdout-w-flush-going-on-in-python-threading
# https://github.com/nextcloud/server/issues/23568 (files_external:applicable)

