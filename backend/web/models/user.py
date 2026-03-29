import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, localtime


def photo_upload_to(instance,filename):
    # 取文件的后缀扩展名（jpg）
    ext = filename.split('.')[-1]
    # hex是取十六进制
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'
    return f'user/photos/{instance.user_id}_{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='user/photos/default.jpg', upload_to=photo_upload_to)
    profile = models.TextField(default='谢谢你的关注',max_length=500)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.user.username} - {localtime(self.create_time).strftime("%Y-%m-%d %H:%M:%S")}'