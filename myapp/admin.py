
from django.contrib import admin
from . models import Faq,Eoi,Tender,Gallery,Video,PrivitasationUsers,AvailableOpening,News,RecentActivities,BoardMember,Management, AccessToInformation, Policy, ProcurementReport,MDNote, ChairmanNote, PressRelease, WebStory, PSSpeech,SuccessStory



admin.site.site_header = "Privatization Commission Admin"
admin.site.site_title = "Privatization Commission Admin Portal"
admin.site.index_title = "Welcome to the PC Admin Dashboard"

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Tender)
admin.site.register(Faq)
admin.site.register(Eoi)
admin.site.register(Video)
admin.site.register(PrivitasationUsers)
admin.site.register(AvailableOpening)
admin.site.register(News)
admin.site.register(RecentActivities)
admin.site.register(BoardMember)
admin.site.register(Management)
admin.site.register(AccessToInformation)
admin.site.register(Policy)
admin.site.register(ProcurementReport)

admin.site.register(MDNote)
admin.site.register(ChairmanNote)
admin.site.register(PressRelease)
admin.site.register(WebStory)
admin.site.register(PSSpeech)
admin.site.register(SuccessStory)
