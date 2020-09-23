from django.db import models


class Band(models.Model):

    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=200)


class Album(models.Model):

    class Meta:
        db_table = 'album'

    title = models.CharField(max_length=200)
    band = models.ForeignKey(Band, related_name='albuns', on_delete=models.CASCADE)
    date = models.DateField()


class Member(models.Model):

    class Meta:
        db_table = 'member'

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey(Band, related_name='members', on_delete=models.CASCADE)


class Music(models.Model):

    class Meta:
        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
