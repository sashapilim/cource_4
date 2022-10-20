from typing import Optional

from project.dao.main_dao import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')


    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_fresh(page=page, filter=filter)
