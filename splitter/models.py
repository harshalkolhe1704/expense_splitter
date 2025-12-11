from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.TextField(help_text="Comma-separated list of participants")
    share_per_person = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate share before saving
        if self.participants and self.amount:
            # Split by comma and strip whitespace
            participant_list = [p.strip() for p in self.participants.split(',') if p.strip()]
            count = len(participant_list)
            if count > 0:
                self.share_per_person = self.amount / count
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.amount}"
