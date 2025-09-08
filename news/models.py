from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Maqola nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Maqola matni")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasmi")
    video = models.FileField(upload_to="videos/", null=True, blank=True, verbose_name="Videosi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Bo'lim")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created']


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Matni")
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Maqola")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Avtor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqti")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created']