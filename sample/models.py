from django.db import models
from service.models import ServiceType, Technology

# Create your models here.
def sample_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'sample/{0}/{1}'.format(self.id, filename)

class ProductSample(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=None)
    technology = models.ForeignKey(to=Technology, on_delete=models.CASCADE)
    service_type = models.ForeignKey(to=ServiceType, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to=sample_directory_path, null=True)
    is_active = models.BooleanField(default=True)
    url_preview = models.CharField(max_length=200, blank=True)