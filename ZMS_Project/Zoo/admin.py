from django.contrib import admin
from .models import Animal,Department,Staff,WorksIn,LivesIn,LooksAfter,Exhibit

# Register your models here.
admin.site.register(Animal)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Exhibit)
admin.site.register(WorksIn)
admin.site.register(LivesIn)
admin.site.register(LooksAfter)
