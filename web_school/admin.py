
from django.contrib import admin
from .models import *
admin.site.site_title="masera"
admin.site.site_header="masera"
admin.site.register(Class)
admin.site.register(Content)
admin.site.register(Duty)
admin.site.register(Explain)
admin.site.register(Exam)
admin.site.register(Summary)
# admin.site.register(Unit)
admin.site.register(User)
# admin.site.register(ClassPivotContent)
# Register your models here.
