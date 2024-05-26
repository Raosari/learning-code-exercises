from django.db import models

# Create your models here.
class Profile(models.Model):
    #name, slug, bg-color
    BG_CHOICES = (
        ("brown", "Brown"),
        ("pink", "Pink"),
        ("orange", "Orange"),
        ("red", "Red"),
        ("yellow", "Yellow"),
        ("green", "Green"),
        ("blue", "Blue"),
    )
    name = models.CharField(verbose_name="name", max_length=50)
    slug = models.SlugField(verbose_name="slug",max_length=100)
    bg_color = models.CharField(verbose_name="color",max_length=20,choices=BG_CHOICES)


    def __str__(self) -> str:
        return self.name



class Link(models.Model):
    text = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")
