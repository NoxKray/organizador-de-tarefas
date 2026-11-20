from datetime import datetime

class GerenciadorDeTarefas:
    def __init__(self, User: str):
        self.User = User
        self.Register = {}

    def criar_tarefa(self, nomedatarefa: str):
        if nomedatarefa in self.Register:
            print('ja existe uma tarefa com esse nome, utilize outro\n')
        else:
            print(f"tarefa criada: {nomedatarefa}\n")
            self.Register[nomedatarefa] = datetime.now()

    def excluir_tarefa(self, nomedatarefa):
        if nomedatarefa in self.Register:
            del self.Register[nomedatarefa]
            print(f"tarefa excluída com sucesso: {nomedatarefa}\n")
            return True


