from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL) в книге
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(unique=True, verbose_name='Email')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=30, blank=True,verbose_name="Населённый пункт")
    photo = models.ImageField(upload_to='users/%Y-%m-%d', blank=True,verbose_name="Фото")
    #photo = models.ImageField(upload_to='users/', blank=True, verbose_name="Фото")
    # пол
    sex_choices = (
        ('male', 'мужской'),
        ('female', 'женский'),
    )
    sex = models.CharField(max_length=10, choices=sex_choices, default='male', verbose_name="пол")

    # социальный статус школьник студент работающий, бизнесмен и тд
    social_status_choices = (
        ('schoolboy', 'Школьник'),
        ('student', 'Студент'),
        ('working', 'Рабочий'),
        ('сivil_servant', 'Госслужащий'),
        ('businessman', 'Предприниматель'),
        ('unemployed', 'Безработный'),
        ('other', 'Другое'),
    )
    social_status = models.CharField(max_length=20, choices=social_status_choices, default='other', verbose_name="Социальный статус")
    status_choices = (
        ('blocked', 'Заблокирован'),
        ('activated', 'Активный'),
        ('waits for activation', 'Ожидает активацию'),
    )
    status = models.CharField(max_length=50, choices=status_choices, default='waits for activation',  verbose_name="Статус")

    phone = models.CharField(max_length=12, verbose_name="Телефон")  # +7 XXX XXX XXXX

    class Meta:
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        # unique_together = ["phone", User.email ]

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

        # @receiver(post_save, sender=User)
        # def create_user_profile(sender, instance, created, **kwargs):
        # if created:
        # Profile.objects.create(user=instance)

        # @receiver(post_save, sender=User)
        # def save_user_profile(sender, instance, **kwargs):
        # instance.profile.save()


        # class Profile(models.Model):
        #     ## идентификатор пользователя
        #     user = models.OneToOneField(User, on_delete=models.CASCADE)
        #     ## имя
        #     first_name = models.CharField(max_length=30)
        #     ## фамилия
        #     last_name = models.CharField(max_length=30)
        #     ## пол
        #     sex_choices = (
        #         ('male', 'male'),
        #         ('female', 'female'),
        #     )
        #     sex = models.CharField(max_length=10, choices=sex_choices, default='male')
        #     ##телефон
        #     # phone =
        #     ##социальный статус школьник студент работающий, бизнесмен и тд
        #     social_status_choices = (
        #         ('schoolboy', 'schoolboy'),
        #         ('student', 'student'),
        #         ('working', 'working'),
        #         ('businessman', 'businessman'),
        #         ('other', 'other'),
        #     )
        #     social_status = models.CharField(max_length=20, choices=social_status_choices, default='other')
        #     ##заблокирован аккаунт или нет
        #     status_choices = (
        #         ('blocked', 'blocked'),
        #         ('activated', 'activated'),
        #         ('waits for activation', 'waits for activation'),
        #     )
        #     status = models.CharField(max_length=50, choices=status_choices, default='waits for activation')
        #     ##город
        #     city = models.CharField(max_length=30, blank=True)
        #     ##дата рождения
        #     birthday = models.DateField(null=True, blank=True)
        #     ##почта
        #     email = models.EmailField(max_length=50)
        #     ##дата и время регистрации
        #     date_registrate = models.DateTimeField(auto_now_add=True)
        #
        #     # аватар
        #     # avatar = models.ImageField(storage = fs )
        #     # current_user.ip_address = request.META['REMOTE_ADDR']
        #     # пароль
        #     # password = models.CharField
        #
        #     @receiver(post_save, sender=User)
        #     def create_or_update_user_profile(sender, instance, created, **kwargs):
        #         if created:
        #             Profile.objects.create(user=instance)
        #         instance.profile.save()
        # created = models.DateTimeField(auto_now_add=True)
        # updated = models.DateTimeField(auto_now=True)
        #     class Meta:
        #         verbose_name_plural = 'profiles'
        #         ordering = ['date_registrate']  # упорядочивание по дате регистрации
        #
        #     def __str__(self):
        #         return self.first_name
