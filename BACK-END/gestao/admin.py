from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccounts, Movies, Series, UserProfiles

class UserAccountsAdmin(UserAdmin):
    model = UserAccounts
    list_display = ('id','username', 'plans' )
    fieldsets = ( 
        ('Required', {'fields': ('username', 'password','profiles', 'plans')}), 
        ('Personal', {'fields': ('first_name', 'last_name', 'email')}), # 
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ), 
    )
    search_fields = ('username', 'plans')
    ordering = ('-id',)

admin.site.register(UserAccounts, UserAccountsAdmin) # Registrando na area do ADMIN

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'launch_date', 'genre', 'rated')
    search_fields = ('title', 'launch_date', 'genre', 'rated')
    ordering = ('-id',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'launch_date', 'genre', 'rated')
    search_fields = ('title', 'launch_date', 'genre', 'rated')
    ordering = ('-id',)

@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account_owner')
    search_fields = ('name', 'account_owner')

    def account_owner(self, obj):
        owner = UserAccounts.objects.filter(id=obj.account).first()
        return owner.username
        
