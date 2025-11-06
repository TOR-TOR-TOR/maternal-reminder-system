from django.db import models

# Create your models here.

class BaseModel(models.Model):
    
    """
    Abstract base model that gives every table:
    - created_at: when it was first made
    - updated_at: when it was last changed
    - is_active: soft delete toggle
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True  # makes sure Django doesn’t create a table for this

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id})"
