from django.db import models

# Create your models here.

class critic(models.Model):
    critic_id = models.AutoField
    critic_name = models.CharField(max_length=50)
    critic_email = models.EmailField(default='none')
    critic_question = models.TextField()

    def __str__(self):
        return 'Message from ' + self.critic_name