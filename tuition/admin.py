from django.contrib import admin
from .models import Contact,Post,Subject,Class_in
from django.utils.html import format_html
from django.utils import timezone

# Register your models here.
admin.site.site_header = "Tuition Admin"
admin.site.site_title = "Tuition Admin Panel"
admin.site.index_title = ""

class PostAdmin(admin.ModelAdmin):
    # fields = ('user')
    # exclude = ('slug',)
    readonly_fields = ('slug',)
    list_display = ('user', 'title','titile_html_display','created_at','get_class_in','get_subjects','slary','created_since',)
    list_filter = ('created_at','subject','class_in')
    search_fields = ('details','user__username', 'subject__name', 'class_in__name')
    filter_horizontal = ('subject','class_in')
    list_editable = ('slary',)
    list_display_links = ('user','title',)

    actions = ('change_salary_3000',)
    def change_salary_3000(self, request, queryset):
        count = queryset.update(slary=3000.0)
        self.message_user(request, '{} posts updated'.format(count))
    change_salary_3000.short_description = 'Change salary to 3000'

    def created_since(self, Post):
        diff = timezone.now() - Post.created_at
        return diff.days
    created_since.short_description = 'Since Created'

    def get_subjects(self, obj):
        return ", ".join([p.name for p in obj.subject.all()])
    get_subjects.short_description = 'Subjects'

    def get_class_in(self, obj):
        return ", ".join([p.name for p in obj.class_in.all()])
    get_class_in.short_description = 'Classes'

    def titile_html_display(self, obj):
        return format_html(
            f'<span style="font-size: 12px; color:blue;">{obj.title}</span>'
        )    


admin.site.register(Contact)
admin.site.register(Post, PostAdmin)
admin.site.register(Subject)
admin.site.register(Class_in)
