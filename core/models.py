from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib import messages
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100, null=False,
                            default='uncategorized',)
    description = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = ("Category")

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="images/Books", default='default.jpg')
    author = models.CharField(max_length=100, null=False)
    first_added = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=False, default=0)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        # on creating a new book for the first time, a date of creation is added.
        if not self.id:
            self.first_added = timezone.now()
        self.modified = timezone.now()
        return super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = ("Add Book")

    def __str__(self) -> str:
        return self.name


class Issued(models.Model):
    taker = models.CharField(max_length=200, null=False)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", default='default.jpg')
    # phone_regex = RegexValidator(regex=r'^[0-9]{10}$"', message="Invalid Number")
    phone_number = models.CharField(max_length=10, blank=True)
    date_of_issue = models.DateTimeField(editable=False, null=True)
    has_returned = models.BooleanField(default=False)
    date_of_return = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_of_issue = timezone.now()
        if self.has_returned == True:
            book_instance = Book.objects.get(name=self.book_name)
            print(book_instance)
            book_instance.quantity = book_instance.quantity + 1
            book_instance.save()
            instance = Issued.objects.get(id=self.id)
            instance.delete()
            # self.date_of_return = timezone.now()

        # On issuing a book, the quantity of Books has to be reduced

        try:
            book_instance = Book.objects.get(name=self.book_name)
            if not self.id and book_instance.quantity >= 1:
                print(book_instance.quantity)
                if book_instance is not None:
                    book_instance.quantity = book_instance.quantity - 1
                    book_instance.save()
                    return super(Issued, self).save(*args, **kwargs)
                else:
                    messages.add_message('Error finding book')
        except Exception as e:
            pass

    class Meta:
        verbose_name = ("Issue Book To")
        verbose_name_plural = ("Issue Book To")
        # verbose_name_plural = ("Issueds")

    def __str__(self):
        return self.taker

# Image compressor Signal


def image_compressor(sender, **kwargs):
    if kwargs["created"]:
        with Image.open(kwargs["instance"].image.path) as photo:
            photo.save(kwargs["instance"].image.path,
                       optimize=True, quality=50)


post_save.connect(image_compressor, sender=Book)
post_save.connect(image_compressor, sender=Issued)
