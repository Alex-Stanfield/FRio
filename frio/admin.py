from django.contrib import admin

from .models import Camaras, Umbrales

# Register your models here.


admin.site.register(Camaras)
admin.site.register(Umbrales)

# @admin.action(description='Sync with Pharaoh')
# def sync_pharaoh(modeladmin, request, queryset):

#     # param_cecos = ''
#     # for cc in Ceco.objects.all().values_list('CC', flat=True):
#     #     param_cecos += cc + ','
#     # param_cecos = param_cecos[:-1]

#     # print(param_cecos)

#     ccl = PhCecos.objects.raw(PhCecos.QUERY) #.format(param_cecos))

#     for cc in ccl:

#         ceco =  Ceco(CC=cc.CC, desc=cc.desc.title())
#         ceco.save()
#         # print(cc)

#     # queryset.update(status='p')


# class CecoAdmin(admin.ModelAdmin):
#     list_display = ['CC', 'desc']
#     ordering = ['CC']
#     actions = [sync_pharaoh]

# admin.site.register(Ceco, CecoAdmin)


# admin.site.register(Usuario)

# # Define an inline admin descriptor for Umbrales model
# # which acts a bit like a singleton
# class UsuarioInline(admin.StackedInline):
#     model = Usuario
#     can_delete = False
#     verbose_name_plural = 'Usuarios'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UsuarioInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
