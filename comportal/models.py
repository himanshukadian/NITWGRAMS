from django.db import models
from django.urls import reverse
from users_auth.models import CustomUser


class Complain(models.Model):
    title = models.CharField(max_length=200)
    CATEGORY_CHOICES = (
        ('E', 'electrical'),
        ('P', 'plumber'),
        ('C', 'carpenter'),
        ('H', 'housekeeping'),
        ('D', 'healthcare'),
        ('M', 'Mess'),
    )

    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default='H'
    )

    TYPE_CHOICES = (
        ('I', 'individual'),
        ('G', 'general'),

    )
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='G'
    )
    pimage = models.ImageField(default='download.jpg', upload_to='')
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    by = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='profile')
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comportal:detail', kwargs={'pk': self.pk})
def get_image_filename(self, filename):
    title = instance.complain.title
    slug = slugify(title)
    return "complain_images/%s-%s" % (slug, filename)


class Image(models.Model):
    complain = models.ForeignKey(Complain,on_delete = models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Image')
class Post(models.Model):
    complain = models.ForeignKey(Complain, on_delete = models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    by = models.CharField(max_length=50)

    def __str__(self):
        return self.text