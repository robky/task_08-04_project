from rest_framework import serializers
from .models import Post, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('slug',)


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer(required=False, many=False)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        model = Post

    def create(self, validated_data):
        # Если в исходном запросе не было поля achievements
        if 'group' not in self.initial_data:
            # То создаём запись о котике без его достижений
            post = Post.objects.create(**validated_data)
            return post

        # Иначе делаем следующее:
        # Уберём список достижений из словаря validated_data и сохраним его
        slug = validated_data.pop('group')
        # Сначала добавляем котика в БД
        group = Group.objects.get(slug=slug)
        if group:
            post = Post.objects.create(group=group, **validated_data)
            return post

    # def create(self, validated_data):
    #     slug = validated_data.pop('group')
    #     if slug:
    #         group = Group.objects.get(slug=slug)
    #     post = Post.objects.create(group=group, **validated_data)
    #     return post


'''
Настройте API для Yatube так, чтобы при запросе постов возвращалась информация 
о группе, в которой опубликован пост. Данные о группе должны возвращаться в 
виде значения её поля slug.

Добавьте возможность при создании или изменении поста через API опционально 
указывать группу, передавая в теле запроса поле slug.
'''
