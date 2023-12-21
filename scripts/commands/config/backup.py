import scripts.commands.execute as execute
import os

class Backup():

    def execute(self):
        # Configura backup:
        # Desabilita o app files_versions, pois o mesmo causa problema na conexão com o servidor de backup
        execute.command("docker-compose exec -u www-data nextcloud php occ app:disable files_versions")

        # Instala aplicativos 'files_external' e 'backup'
        execute.command("docker-compose exec -u www-data nextcloud php occ --no-warnings app:install files_external")
        execute.command("docker-compose exec -u www-data nextcloud php occ --no-warnings app:install --force backup")
        
        # Ativa aplicativos 'files_external' e 'backup'
        execute.command("docker-compose exec -u www-data nextcloud php occ --no-warnings app:enable files_external")
        execute.command("docker-compose exec -u www-data nextcloud php occ --no-warnings app:enable --force backup")

        # Importa configurações do ponto de monstagem externo

        HN = os.getenv("MINIO_HOSTNAME"); P = os.getenv("MINIO_PORT")
        SSL = os.getenv("MINIO_USE_SSL"); UPS = os.getenv("MINIO_USE_PATH_STYLE")
        K = os.getenv("MINIO_ROOT_USER"); S = os.getenv("MINIO_ROOT_PASSWORD")
        config = "-c bucket=nextcloud"
        config += f" -c hostname={HN}"
        config += f" -c port={P}"
        config += f" -c use_ssl={SSL}"
        config += f" -c use_path_style={UPS}"
        config += f" -c key={K}"
        config += f" -c secret={S}"

        command_create_file_external = f"docker-compose exec -u www-data nextcloud php occ files_external:create {config} Backup amazons3 amazons3::accesskey"
        execute.command(command_create_file_external)
        execute.command("docker-compose exec -u www-data nextcloud php occ files_external:applicable --add-group admin 1")
        print("Backup configurado! \u2705")

## https://doc.owncloud.com/server/next/admin_manual/configuration/server/occ_command.html#files_externalcreate