from abc import ABC, abstractmethod
from typing import List, Dict

# Interface para operações de leitura
class LivroReaderInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

# Interface para operações de Escrita
class LivroWriterInterface(ABC):
    @abstractmethod
    def add(self, livro_data: Dict) -> Dict:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    def update(self, id: int, livro_data: Dict) -> bool:
        pass

class LivroRepositoryInterface(LivroReaderInterface, LivroWriterInterface):
    pass