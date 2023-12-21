import scripts.commands.execute as execute
import os

# docker exec -u www-data nextcloud php occ --no-warnings config:system:set trusted_domains 1 --value=nextcloud
# docker exec -u www-data nextcloud php occ --no-warnings config:system:set trusted_domains 2 --value=lab

class Enable_Onlyoffice():
    def execute(self):
        execute.command("docker exec -u www-data nextcloud php occ --no-warnings app:install onlyoffice")
        execute.command("docker exec -u www-data nextcloud php occ --no-warnings config:system:set onlyoffice DocumentServerUrl --value=\"/ds-vpath/\"")
        execute.command(f"docker exec -u www-data nextcloud php occ --no-warnings config:system:set onlyoffice DocumentServerInternalUrl --value=\"http://{os.getenv('ONLYOFFICE_HOSTNAME')}/\"")
        execute.command(f"docker exec -u www-data nextcloud php occ --no-warnings config:system:set onlyoffice StorageUrl --value=\"http://{os.getenv('NGINX_HOSTNAME')}/\"")
        execute.command(f"docker exec -u www-data nextcloud php occ --no-warnings config:system:set onlyoffice jwt_secret --value=\"{os.getenv('ONLYOFFICE_JWT_SECRET')}\"")