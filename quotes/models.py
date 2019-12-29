from django.db import models
import datetime

class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Quote(models.Model):
    quote = models.TextField(null=True)
    author = models.CharField(max_length=200,null=True)
    #created_at = models.DateTimeField(auto_now_add=True,null=True)
    #updated_at = models.DateTimeField(auto_now=True,null=True)
    created = models.DateTimeField(editable=False,null=True)
    modified = models.DateTimeField(null=True)

    quote_category = models.ForeignKey(
        'QuoteCategory',
        on_delete= models.CASCADE
    )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Quote, self).save(*args, **kwargs)

    def __str__(self):
        if len(self.quote) >50 :
            return self.quote[:50] + "..."
        return self.quote






