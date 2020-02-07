from django.contrib.auth.forms import UserCreationForm
from usuario.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']