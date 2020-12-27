from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler
from typing import List


class GetTodoAllRequest(BaseRequest):
    pass


class GetTodoAllResponse(BaseResponse):
    def __init__(self, id: int, title: str):
        self.id: int = id
        self.title: str = title


class GetTodoAllUseCase(BaseHandler):

    async def handle(self, req: GetTodoAllRequest) -> List[GetTodoAllResponse]:
        response = [GetTodoAllResponse(id="id", title="title")]

        return response
