from django.db import models

class ProjectCard(models.Model):
    demoUrl = models.URLField(max_length=200)
    github = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=100)
    gif = models.URLField(max_length=200)
    description = models.TextField()
    icons = models.CharField(max_length=200)
    cardLang = models.CharField(max_length=200)
    isDesign = models.BooleanField(default=False)
