from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    todo = models.ForeignKey(
        'todos.Todo', related_name='comments', on_delete=models.CASCADE, blank=True)
    contents = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.contents
