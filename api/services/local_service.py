from api.models import Local


def listar_local_usuario(usuario_id):
    return Local.objects.filter(usuario_id=usuario_id).first()


def search_by_name(name):
    return Local.objects.filter(nome__icontains=name).all()
