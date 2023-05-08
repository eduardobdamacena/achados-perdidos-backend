from api.models import User


def listar_usuario_id(usuario_id):
    return User.objects.get(id=usuario_id)


def apagar_usuario_id(usuario_id):
    usuario = listar_usuario_id(usuario_id)
    usuario.delete()
