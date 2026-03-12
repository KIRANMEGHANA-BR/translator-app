from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import TranslationHistory

@admin.action(description="Mark selected translations as favorite")
def make_favorite(modeladmin, request, queryset):
    queryset.update(is_favorite=True)

@admin.action(description="Unmark selected translations as favorite")
def remove_favorite(modeladmin, request, queryset):
    queryset.update(is_favorite=False)

@admin.action(description="Export selected translations as CSV")
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=translations.csv'
    writer = csv.writer(response)
    writer.writerow(['User', 'Original Text', 'Translated Text', 'Source Lang', 'Target Lang', 'Favorite', 'Created At'])
    for t in queryset:
        writer.writerow([t.user, t.original_text, t.translated_text, t.source_language, t.target_language, t.is_favorite, t.created_at])
    return response

@admin.register(TranslationHistory)
class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_text_short', 'translated_text_short', 'source_language', 'target_language', 'is_favorite', 'created_at')
    list_filter = ('source_language', 'target_language', 'is_favorite', 'created_at')
    search_fields = ('original_text', 'translated_text')
    ordering = ('-created_at',)
    actions = [make_favorite, remove_favorite, export_as_csv]

    # Shorten long texts in admin display
    def original_text_short(self, obj):
        return obj.original_text[:50] + ('...' if len(obj.original_text) > 50 else '')
    original_text_short.short_description = 'Original Text'

    def translated_text_short(self, obj):
        return obj.translated_text[:50] + ('...' if len(obj.translated_text) > 50 else '')
    translated_text_short.short_description = 'Translated Text'