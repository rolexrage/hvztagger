from django.contrib import admin
from django import forms
from django.conf import settings
from django.http import HttpResponse
from uchicagohvz.game.models import *

# Register your models here.

admin.site.register(Game)

class PlayerAdmin(admin.ModelAdmin):
	list_filter = ('game', 'active', 'human', 'dorm', 'renting_gun', 'gun_requested', 'gun_returned', 'major')
	if not settings.DEBUG:
		readonly_fields = ('major',)
	search_fields = ('user__username', 'user__first_name', 'user__last_name', 'bite_code')
	actions = ['players_to_csv']

	def players_to_csv(ma, request, players):
		response = HttpResponse(content_type='text/plain')
		header = ['NAME', 'USERNAME', 'EMAIL', 'PHONE_NUMBER', 'GAME', 'ACTIVE', 'DORM', 'RENTING_GUN', 'GUN_RETURNED']
		response.write(','.join(header) + '\n')
		for p in players.order_by('user__last_name', 'user__first_name'):
			data = (
				p.user.get_full_name(),
				p.user.username,
				p.user.email,
				p.user.profile.phone_number,
				p.game.name,
				str(p.active),
				p.get_dorm_display(),
				str(p.renting_gun),
				str(p.gun_returned)
			)
			response.write(','.join(data) + '\n')
		return response
	players_to_csv.short_description = 'Export to CSV'

class KillAdminForm(forms.ModelForm):
	def clean(self):
		cleaned_data = super(KillAdminForm, self).clean()
		if cleaned_data['killer'].game != cleaned_data['victim'].game:
			raise forms.ValidationError('Killer and victim games do not match.')
		return cleaned_data

class KillAdmin(admin.ModelAdmin):
	form = KillAdminForm
	list_filter = ('killer__game',)
	readonly_fields = ('parent',)
	search_fields = ('killer__user__username', 'killer__user__first_name', 'killer__user__last_name', 
		'victim__user__username', 'victim__user__first_name', 'victim__user__last_name')

admin.site.register(Squad)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Kill, KillAdmin)
admin.site.register(Award)
admin.site.register(HighValueTarget)
admin.site.register(HighValueDorm)
