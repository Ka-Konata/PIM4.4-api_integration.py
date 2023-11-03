from api_integration.utils import get_value

class Disciplina:
    """Model para a entidade Disciplina."""

    def __init__(self, 
                 nome: str,
                 id: int = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.nome = nome

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Disciplina(
            id=get_value(content, "id"),
            nome=get_value(content, "nome")
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "nome": self.nome
        }
    
    def to_context(self) -> dict:
        """Converte o objeto atual em um discionário. para inserir em um context"""
        return {
            "id": self.id,
            "nome": self.nome
        }

    @property # retorna o valor encapsulado
    def id(self) -> int:
        return self.__id
