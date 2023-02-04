from api.models import Local


def listar_local_usuario(usuario_id):
    return Local.objects.filter(usuario_id=usuario_id).first()
