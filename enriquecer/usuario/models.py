from django.db import models

class Usuario(models.Model):
    user = models.CharField(max_length=20)
    passw = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else 'sem data'}"
