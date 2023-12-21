import scripts.commands.execute as execute
import os

class Theme():
    def execute(self):
        # Configura o tema da aplicação
        execute.command(f"docker-compose exec -u www-data nextcloud php occ theming:config name \"{os.getenv('NAME_OF_SERVER')}\"")
        execute.command("docker-compose exec -u www-data nextcloud php occ theming:config slogan \"Implementado por Rubens Jr\"")
        execute.command("docker-compose exec -u www-data nextcloud php occ theming:config disable-user-theming \"true\"")
        execute.command("docker-compose exec -u www-data nextcloud php occ theming:config logo \"/var/www/resources/logo.svg\"")
        execute.command("docker-compose exec -u www-data nextcloud php occ theming:config logoheader \"/var/www/resources/logo.svg\"")
        execute.command("docker-compose exec -u www-data nextcloud php occ theming:config favicon \"/var/www/resources/logo.svg\"")