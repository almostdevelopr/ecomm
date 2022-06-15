from django.db import models

# Create your models here.
class Category(models.Model):
    """A class to represent category model."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    # TODO: Return a proper name
    def __str__(self):
        """Return string representation of the model."""
        return str(self.name)
