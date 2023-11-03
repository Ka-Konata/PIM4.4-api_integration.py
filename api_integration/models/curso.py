from . disciplina import Disciplina
from api_integration.utils import get_value

class Curso:
    """Model para a entidade Curso."""

    def __init__(self, 
                 nome: str,
                 carga_horaria: int,
                 aulas_totais: int,
                 id: int = None,
                 disciplinas: list[Disciplina] = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__disciplinas = disciplinas
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_totais = aulas_totais

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        # Instanciando cada disciplina para o objeto.
        disciplinas = []
        if get_value(content, "disciplinas") != None:
            for d in get_value(content, "disciplinas"):
                disciplinas.append(Disciplina.by_dict(d))

        return Curso(
            id=get_value(content, "id"),
            nome=get_value(content, "nome"),
            carga_horaria=get_value(content, "cargaHoraria"),
            aulas_totais=get_value(content, "aulasTotais"),
            disciplinas=disciplinas
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "nome": self.nome,
            "cargaHoraria": self.carga_horaria,
            "aulasTotais": self.aulas_totais
        }
    
    def to_context(self) -> dict:
        """Converte o objeto atual em um discionário para inserir em um context."""
        # Previamente é necessário converter cada disciplina em discionarios também.
        disciplinas = []
        if self.disciplinas != None:
            for d in self.disciplinas:
                disciplinas.append(d.to_dict())

        return {
            "id": self.id,
            "nome": self.nome,
            "carga_horaria": self.carga_horaria,
            "aulas_totais": self.aulas_totais,
            "disciplinas": disciplinas
        }

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id
    
    @property
    def disciplinas(self) -> list[Disciplina]:
        return self.__disciplinas
    
    @disciplinas.setter # Altera o valor encapsulado
    def disciplinas(self) -> None:
        pass # Ainda para implementarclass Add_Disciplina_Em_Curso:

    class Disicplina_Em_Curso:
        """Model para inserir uma disciplina em um curso"""
        def __init__(self,
                    id_curso: int,
                    id_disciplina: int) -> None:
            """Construtor da classe"""
            self.id_curso = id_curso
            self.id_disciplina = id_disciplina

        def to_dict(self) -> dict:
            return {
                "idCurso": self.id_curso,
                "idDisciplina": self.id_disciplina
            }
