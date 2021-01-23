from rest_framework import serailizers
from django.contrib.auth.models import User
from django.contrib.auth.models import Publ
from django.contrib.auth.models import Rea
from django.contrib import messages


class UserSerializer(serailizers.Serailizer):
    id = serailizers.ReadOnlyField()
    username = serailizers.CharField()
    password = serailizers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serailizers.ValidationError("Este usuario ya existe")
        else:
            return data


class PublicacionSerializer(serailizers.Serailizer):
    id = serailizers.ReadOnlyField()
    publicacion = serailizers.TextField()

    def publicacion(self, publicacion):
        instance = Publ()
        instance = serailizers.publicacion.CharField('publicacion')
        instance.save()
        return instance

    def validate_publ(self, data, request):
        publs = Publ.objects.filter(publs=data)

        if publs == 0:
            raise serailizers.ValidationError("ingrese Publicacion")
            publs
        else:
            messages.success(request, 'Su publicacion a sido creada')
            return data


class reaccionSerializer(serailizers.Serailizer):
    a = ['Like', 'I dont like', 'I love it', 'amazes me', 'sad me']
    reaccion = serailizers.TextField()

    def create_reaccion(self, data, request):

        a = ['Like', 'I dont like', 'I love it', 'amazes me', 'sad me']
        instance = Rea()
        instance = serailizers.publicacion.TextField('reaccion')
        if instance == a['like']:
            return instance
            instance.save()
        elif instance == a['I dont like']:
            return instance
        elif instance == a['I love it']:
            return instance
        elif instance == a['amazes me']:
            return instance
        elif instance == a['sad me']:
            return instance
        else:
            return data


class CommentSerializer(serailizers.Serailizer):
    owner = serailizers.ForeignKey(UserSerializer)
    post = serailizers.ForeignKey(PublicacionSerializer)
    text = serailizers.CharField(max_length=300)
    reaccion = serailizers.BooleanField(reaccionSerializer)

    def __str__(self):
        return self.text
