from django.contrib import admin
# Import all models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Enrollment, Submission

# Inline for Lessons
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Inline for Questions
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

# Inline for Choices
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

# Course Admin with Lessons and Questions inlines
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Question Admin with Choices inline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course']
    search_fields = ['content']

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register all models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)