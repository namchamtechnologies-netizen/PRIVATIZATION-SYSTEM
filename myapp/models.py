from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords

class CustomHistoricalRecords(HistoricalRecords):
    def get_history_record(self, instance):
        history_instance = super().get_history_record(instance)
        history_instance.custom_str = f'{history_instance.history_date} - {history_instance.history_user} - {history_instance.history_type} - TITLE: {history_instance.title}'
        return history_instance

# Base model for common fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# Gallery Model
class Gallery(BaseModel):
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=100, blank=True, null=True)
    history = CustomHistoricalRecords()

    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Gallery Items"
        
    def __str__(self):
        return self.title or f"Gallery Item {self.id}"

# Video Model
class Video(BaseModel):
    video_url = models.URLField(default="")
    title = models.CharField(max_length=100, blank=True, null=True)
    history = CustomHistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title or f"Video {self.id}"

# Users Model
class PrivitasationUsers(models.Model):
    email = models.EmailField()
    password = models.TextField()
    name = models.CharField(max_length=30, blank=True, null=True)
    kra = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

# Available Opening Model
class AvailableOpening(BaseModel):
    title = models.CharField(max_length=255)
    date_today = models.DateField()
    link_to_opening = models.URLField(blank=True, null=True)
    department = models.CharField(max_length=255, null=True)
    history = CustomHistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Available Openings"

    def __str__(self):
        return self.title

# News Model
class News(BaseModel):
    title = models.CharField(max_length=255)
    date_today = models.DateField()
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    history = CustomHistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

# Recent Activities Model
class RecentActivities(BaseModel):
    title = models.CharField(max_length=255)
    date_today = models.DateField()
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    link_url = models.URLField(blank=True, null=True)
    history = CustomHistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Recent Activities"

    def __str__(self):
        return self.title

# Board Member Model - FIXED with created_at
class BoardMember(BaseModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/')
    
    class Meta:
        ordering = ['created_at']  # Oldest first (maintains upload order)
        verbose_name_plural = "Board Members"
        
    def __str__(self):
        return self.name

# Management Model - FIXED with created_at
class Management(BaseModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='management/')
    
    class Meta:
        ordering = ['created_at']  # Oldest first (maintains upload order)
        verbose_name_plural = "Management"
        
    def __str__(self):
        return self.name

# Access to Information Model
class AccessToInformation(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Access to Information"

    def __str__(self):
        return self.title

# Policy Model
class Policy(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Policies"

    def __str__(self):
        return self.title

# Procurement Report Model
class ProcurementReport(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Procurement Reports"

    def __str__(self):
        return self.title

# MD Note Model
class MDNote(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "MD Notes"

    def __str__(self):
        return self.title

# Chairman Note Model
class ChairmanNote(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Chairman Notes"

    def __str__(self):
        return self.title

# Press Release Model
class PressRelease(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Press Releases"

    def __str__(self):
        return self.title

# Web Story Model
class WebStory(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Web Stories"

    def __str__(self):
        return self.title

# PS Speech Model
class PSSpeech(BaseModel):
    title = models.CharField(max_length=255)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "PS Speeches"

    def __str__(self):
        return self.title

# Success Story Model
class SuccessStory(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='success_stories/')
    description = models.TextField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Success Stories"
        
    def __str__(self):
        return self.title

# Tender Model
class Tender(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    closing_date = models.DateField(null=True, blank=True)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "Tenders"

    def __str__(self):
        return self.title

# EOI Model
class Eoi(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    closing_date = models.DateField(null=True, blank=True)
    document_link = models.URLField()
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name_plural = "EOIs"

    def __str__(self):
        return self.title

# FAQ Model
class Faq(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    class Meta:
        ordering = ['created_at']  # Oldest first (maintains upload order)
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question