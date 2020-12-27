import asyncio

from pydiator_core.mediatr import pydiator
from pydiator_core.serializer import SerializerFactory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.todo.usecases.get_todo_all import GetTodoAllRequest
from app.todo.usecases.get_todo_by_id import GetTodoByIdRequest


@api_view(["GET"])
def get_todo_all(request):
    loop = asyncio.new_event_loop()
    response = loop.run_until_complete(pydiator.send(GetTodoAllRequest()))
    loop.close()

    return Response(SerializerFactory.get_serializer().deserialize(response))


@api_view(["GET", ])
def get_todo_by_id(request, id):
    loop = asyncio.new_event_loop()
    response = loop.run_until_complete(pydiator.send(GetTodoByIdRequest(id=id)))
    loop.close()

    return Response(response.to_json())
