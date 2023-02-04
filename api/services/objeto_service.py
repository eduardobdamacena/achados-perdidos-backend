from api.models import Objeto
from api.services.local_service import listar_local_usuario


def listar_objeto_id(objeto_id):
    objeto = Objeto.objects.get(id=objeto_id)
    return objeto


def listar_objeto_usuario(usuario_id):
    local = listar_local_usuario(usuario_id)
    return Objeto.objects.filter(local_id=local.id).all()


def apagar_objeto(objeto_id):
    objeto = listar_objeto_id(objeto_id)
    objeto.delete()