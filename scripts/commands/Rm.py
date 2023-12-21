import scripts.commands.execute as execute

class Rm():
    def execute(self, option_out):
        repeat = True
        while(repeat == True):
            repeat = False
            execute.command("docker ps --format \"table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\"")
            container_id = input("cole aqui o id do container (ou digite 0 para cancelar): ")
            if(container_id == '0'):
                break
            execute.command(f"docker stop {container_id}")
            execute.command(f"docker rm -v {container_id}")
            if(input("deseja remover algum outro container? (Y/n) ") in ["Y", "y"]):
                repeat = True
        print("")
        return option_out