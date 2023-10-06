# powershell関連のエラーログ

## エラー前
```python
from django.db import models
from django.conf import settings
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name

class Topics(models.Model):
    title = models.CharField(verbose_name="タイトル",max_length=100)
    description = models.TextField(verbose_name="概要")
    created_at = models.DateTimeField("投稿日",auto_now_add=True)
    # models.PROTECTをしていすることで投稿者が消えてもトピックを消さないようにする.
    creted_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                  related_name='account', 
                                  verbose_name="投稿者",
                                  on_delete=models.PROTECT,
                                  default="",
                                  blank=True)
    tags = models.ManyToManyField(Tags,
                                  verbose_name='タグ',
                                  blank=True)
    like_count = models.IntegerField(default=0)
    class Meta:
        db_table = "topics"

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                   related_name='account',
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, 
                              related_name='topics', 
                              verbose_name="トピック",
                              on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comment

```

## エラーログ
```powershell
(venv) PS C:\Users\moyas\Documents\programmes\apps\CivicSeek
> python .\manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
topics.Comments.created_by: (fields.E304) Reverse accessor 'User.account' for 'topics.Comments.created_by' clashes with reverse accessor for 'topics.Topics.creted_by'.
        HINT: Add or change a related_name argument to the definition for 'topics.Comments.created_by' or 'topics.Topics.creted_by'.
topics.Comments.created_by: (fields.E305) Reverse query name for 'topics.Comments.created_by' clashes with reverse query name for 'topics.Topics.creted_by'.
        HINT: Add or change a related_name argument to the definition for 'topics.Comments.created_by' or 'topics.Topics.creted_by'.
topics.Topics.creted_by: (fields.E304) Reverse accessor 'User.account' for 'topics.Topics.creted_by' clashes with reverse accessor for 'topics.Comments.created_by'.
        HINT: Add or change a related_name argument to the definition for 'topics.Topics.creted_by' or 'topics.Comments.created_by'.
topics.Topics.creted_by: (fields.E305) Reverse query name for 'topics.Topics.creted_by' clashes with reverse query name for 'topics.Comments.created_by'.
        HINT: Add or change a related_name argument to the definition for 'topics.Topics.creted_by' or 'topics.Comments.created_by'.
```

## 修正後
- related_nameを変更した

```python
from django.db import models
from django.conf import settings
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name

class Topics(models.Model):
    title = models.CharField(verbose_name="タイトル",max_length=100)
    description = models.TextField(verbose_name="概要")
    created_at = models.DateTimeField("投稿日",auto_now_add=True)
    # models.PROTECTをしていすることで投稿者が消えてもトピックを消さないようにする.
    creted_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                  related_name='topics_account', 
                                  verbose_name="投稿者",
                                  on_delete=models.PROTECT,
                                  default="",
                                  blank=True)
    tags = models.ManyToManyField(Tags,
                                  verbose_name='タグ',
                                  blank=True)
    like_count = models.IntegerField(default=0)
    class Meta:
        db_table = "topics"

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                   related_name='comments_account', 
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, 
                              related_name='topics', 
                              verbose_name="トピック",
                              on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comment
```