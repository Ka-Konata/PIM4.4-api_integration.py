from . professor import Professor
from . aluno import Aluno
from . curso import Curso
from api_integration.utils import get_value

class Turma:
    """Model para a entidade Turma."""

    def __init__(self, 
                 nome: str,
                 curso: Curso,
                 id: int = None,
                 alunos: list[Aluno] = None,
                 professores: list[Professor] = None,
                 coordenador: Professor = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__curso = curso
        self.__alunos = alunos
        self.__professores = professores
        self.nome = nome
        self.coordenador = coordenador

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        # Instanciando cada aluno e professor para o objeto.
        alunos = []
        if get_value(content, "alunos") != None:
            for a in get_value(content, "alunos"):
                alunos.append(Aluno.by_dict(a))

        professores = []
        if get_value(content, "professores") != None:
            for p in get_value(content, "professores"):
                professores.append(Professor.by_dict(p))

        return Turma(
            id=get_value(content, "id"),
            nome=get_value(content, "nome"),
            curso=Curso.by_dict(get_value(content, "curso")),
            alunos=alunos,
            professores=professores,
            coordenador=Professor.by_dict(get_value(content, "coordenador"))
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "nome": self.nome,
            "idCurso": self.curso.id
        }
    
    def to_context(self) -> dict:
        """Converte o objeto atual em um discionário. para inserir em um context"""
        # Previamente é necessário converter cada disciplina, aluno, curso e turma em discionarios também.
        alunos = []
        if self.alunos != None:
            for a in self.alunos:
                alunos.append(a.to_dict())
            
        professores = []
        if self.profesores:
            for p in self.profesores:
                professores.append(p.to_dict())

        return {
            "id": self.id,
            "nome": self.nome,
            "curso": self.curso.to_dict(),
            "alunos": alunos,
            "professores": professores,
            "coordenador": self.coordenador.to_dict()
        }

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id

    @property
    def curso(self) -> Curso:
        return self.__curso

    @property
    def alunos(self) -> list[Aluno]:
        return self.__alunos

    @property
    def professores(self) -> list[Professor]:
        return self.__professores
    
    @curso.setter
    def curso(self) -> None:
        pass # Ainda para implementar
    
    @alunos.setter
    def alunos(self) -> None:
        pass # Ainda para implementar
    
    @professores.setter
    def professores(self) -> None:
        pass # Ainda para implementar