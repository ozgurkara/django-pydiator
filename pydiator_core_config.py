from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer
from pydiator_core.pipelines.log_pipeline import LogPipeline

from app.todo.usecases.get_todo_all import GetTodoAllRequest, GetTodoAllUseCase
from app.todo.usecases.get_todo_by_id import GetTodoByIdRequest, GetTodoByIdUseCase


def set_up_pydiator():
    container = MediatrContainer()
    container.register_pipeline(LogPipeline())

    # Service usecases mapping
    container.register_request(GetTodoAllRequest, GetTodoAllUseCase())
    container.register_request(GetTodoByIdRequest, GetTodoByIdUseCase())

    # Start
    pydiator.ready(container=container)
