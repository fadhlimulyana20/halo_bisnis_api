from django.db import models
from django.contrib.auth.models import User
from service.models import ServiceType, Technology

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'project_design/{0}/{1}'.format(instance.user, filename)

class Project(models.Model):
    name = models.CharField(max_length=100)
    service = models.ForeignKey(to=ServiceType, on_delete=models.CASCADE)
    technology = models.ForeignKey(to=Technology, on_delete=models.CASCADE)
    description = models.TextField(max_length=None)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    is_processed = models.BooleanField(default=False)
    design = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "{} - {}".format(self.name, self.user)