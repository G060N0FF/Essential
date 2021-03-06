# Django imports
from django.db import models
from django.contrib.auth import get_user_model

# database for user's todos
class Todo(models.Model):
	user=models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		related_name='todos',
		null=True
	)
	text=models.CharField(max_length=200)
	complete=models.BooleanField(default=False)
	date=models.DateField(null=True)

# database for user's files
class File(models.Model):
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='files', null=True)
    file=models.FileField(upload_to='files/')