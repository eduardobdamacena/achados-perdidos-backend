from api.models import User


def listar_usuario_id(usuario_id):
    return User.objects.get(id=usuario_id)