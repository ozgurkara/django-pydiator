from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler


class GetTodoByIdRequest(BaseRequest):
    def __init__(self, id: int):
        self.id = id


class GetTodoByIdResponse(BaseResponse):
    def __init__(self, id, title):
        self.id: int = id
        self.title: str = title


class GetTodoByIdUseCase(BaseHandler):
    async def handle(self, req: GetTodoByIdRequest) -> GetTodoByIdResponse:
        return GetTodoByIdResponse(id=req.id, title=f"title {req.id}")
