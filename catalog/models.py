from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.validators import FileExtensionValidator, ImageFileValidator

class User(AbstractUser):
    initials = models.CharField(max_length = 64)
    login = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9-]+$',
                message='Login should contain only letters, numbers, or hyphens.',
                code='invalid_login'
            ),
        ],
    )
    email = models.EmailField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                message='Enter a valid email address.',
                code='invalid_email'
            ),
        ]
    )
    password  = models.CharField(
        max_length=16,
        validators=[MinLengthValidator(8, message='The field must be at least 8 characters long.')]
    )
    is_superadmin = models.BooleanField(default=False)
    def str(self):
        return self.login

class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    image = models.ImageField(
        upload_to='project_images/',
        validators = [
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
            ImageFileValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])
        ]
    )

    date_created = models.DateTimeField(auto_now_add=True)
    designer = models.ForeignKey(User, on_delete=models.CASCADE)
    PROJECT_STATUS = (
        ('n', 'new'),
        ('w', 'in work'),
        ('d', 'done'),
    )
    status = models.CharField(max_length=1, choices=PROJECT_STATUS, default='n')
    SPACE_CATEGORY = (
        ('r', 'Residential Spaces'),
        ('c', 'Commercial Spaces'),
        ('p', 'Public Spaces'),
        ('e', 'Event and Exhibition Spaces'),
        ('g', 'Green Spaces and Landscape Design'),
    )
    space_category = models.CharField(max_length=1, choices=SPACE_CATEGORY)
    PROJECT_CATEGORY = (
        ('3d', '3D Design'),
        ('2d', '2D Design'),
        ('sk', 'Sketch'),
        ('ar', 'Architectural Rendering'),
    )
    project_category = models.CharField(max_length=1, choices=PROJECT_CATEGORY)
    def __str__(self):
        return self.title