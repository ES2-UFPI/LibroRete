# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comentario(models.Model):
    id = models.IntegerField(primary_key=True)
    conteudo = models.CharField(max_length=255)
    data_criacao = models.DateTimeField()
    id_comentario_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='id_comentario_pai', blank=True, null=True)
    id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='id_post')

    class Meta:
        managed = False
        db_table = 'comentario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Interacao(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    data_interacao = models.DateTimeField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='id_post')

    class Meta:
        managed = False
        db_table = 'interacao'


class Lista(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=255)
    id_perfil_lista = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='id_perfil_lista')

    class Meta:
        managed = False
        db_table = 'lista'


class ListaLivro(models.Model):
    id_lista = models.ForeignKey(Lista, models.DO_NOTHING, db_column='id_lista')
    isbn_livro = models.ForeignKey('Livro', models.DO_NOTHING, db_column='isbn_livro')

    class Meta:
        managed = False
        db_table = 'lista_livro'


class Livro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=15)
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'livro'


class Perfil(models.Model):
    id = models.IntegerField(primary_key=True)
    bio = models.CharField(max_length=255)
    interesses = models.TextField()
    id_usuario_perfil = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario_perfil')

    class Meta:
        managed = False
        db_table = 'perfil'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    conteudo = models.CharField(max_length=255)
    #data_criacao = models.DateTimeField()
    midia = models.TextField()

    class Meta:
        managed = False
        db_table = 'post'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=320)
    senha = models.CharField(unique=True, max_length=255)
    foto = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuario'
