from django.db import models



STARS = (
    ('one star', '⭐'),
    ('two stars', '⭐⭐'),
    ('three stars', '⭐⭐⭐'),
    ('four stars', '⭐⭐⭐⭐'),
    ('five stars', '⭐⭐⭐⭐⭐'),
)
# Create your models here.

class Advantages(models.Model):
    name = models.CharField(max_length=50, verbose_name='advaantage')
    info = models.TextField(verbose_name='whats advantage')


    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Advantage'
        verbose_name_plural = "Advantages"
        ordering = ('-created_at',)

    
    def __str__(self):
        return self.name









class Recommend_us(models.Model):
    name = models.CharField(max_length=25, verbose_name='Name Of co-workers')


    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Recommend'
        verbose_name_plural = "Recommends"
        ordering = ('-created_at',)

    
    def __str__(self):
        return self.name









class Help(models.Model):
    name = models.CharField(max_length=50, verbose_name='Help')
    how = models.TextField(verbose_name='How can help')


    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Help'
        verbose_name_plural = "Helps"
        ordering = ('-created_at',)


    def __str__(self):
        return self.name









class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tariff name')
    info = models.CharField(max_length=250, verbose_name='Description')
    photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', blank=True, null=True, verbose_name="photo")
    video = models.FileField(upload_to='post_videos/%Y/%m/%d/', verbose_name="video") #blank=True, null=True, 


    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Tariff'
        verbose_name_plural = "Tariffs"
        ordering = ('-created_at',)


    def __str__(self):
        return self.name









class Review(models.Model):
    name = models.CharField(max_length=25, verbose_name='Name')
    email = models.EmailField(max_length=30, verbose_name='Email/Gmail')
    body = models.CharField(max_length=300, verbose_name='Review')
    stars = models.CharField(max_length=15, choices=STARS, verbose_name='STARS')


    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = "Reviiews"
        ordering = ('-created_at',)


    def __str__(self):
        return self.name









class Integration(models.Model):
    name = models.CharField(max_length=75, verbose_name='Integration')
    info = models.TextField(verbose_name='Info')
    photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', verbose_name="photo")# blank=True, null=True,
    video = models.FileField(upload_to='post_videos/%Y/%m/%d/', blank=True, null=True, verbose_name="video")#blank=True, null=True,
    

    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Integration'
        verbose_name_plural = "Integrations"
        ordering = ('-created_at',)


    def __str__(self):
        return self.name

 







class Opportunity(models.Model):
    name = models.CharField(max_length=75, verbose_name='Ability')
    about = models.CharField(max_length=200, verbose_name='Data')
    

    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Ability'
        verbose_name_plural = "Abilities"
        ordering = ('-created_at',)


    def __str__(self):
        return self.name