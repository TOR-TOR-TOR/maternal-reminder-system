from django.db import models
from django.utils import timezone

class VisitManager(models.Manager):
    def upcoming(self):
        """Return visits with a next visit date in the future."""
        return self.filter(next_visit_date__gte=timezone.now().date())

    def past(self):
        """Return visits that already happened."""
        return self.filter(visit_date__lt=timezone.now().date())

    def for_mother(self, mother):
        """Return all visits related to a specific mother."""
        return self.filter(mother=mother)

    def for_health_worker(self, worker):
        """Return all visits handled by a specific health worker."""
        return self.filter(health_worker=worker)
