from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None,):
        """
        Создает и сохраняет пользователя с заданным адресом электронной почты, датой
        рождение и пароль.
        """
        if not email:
            raise ValueError('Пользователи должны иметь адрес электронной почты')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.role = "user"
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        Создает и сохраняет суперпользователя с указанным адресом электронной почты, датой
        рождение и пароль.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.role = "admin"
        user.save(using=self._db)
        return user
