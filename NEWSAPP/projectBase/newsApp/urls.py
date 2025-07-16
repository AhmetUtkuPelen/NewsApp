from django.urls import path
from .views import*

urlpatterns = [
    # ! langin page url ! #
    path('',index,name="index"),
    # ! global news url ! #
    path('globalnews/',globalNews,name="globalnews"),
    # ! url for displaying the news of admins ! #
    path('readadminnews/<nid>',readadminnews,name="readadminnews"),
    # ! profile page url for users to crate their own news ! #
    path('profile/',profile,name="profile"),
    # ! url for users to read their on and other users' news ! #
    path('usernews/',user_news,name="usernews"),
    # ! spesific user news url ! #
    path('readusernews/<newsId>',read_user_news,name="readusernews"),
    # ! url for users to edit their news ! #
    path('editnews/<newsId>/', edit_user_news, name="editusernews"),
    # ! url for users to delete their news ! #
    path('deletenews/<newsId>/', delete_user_news, name="deleteusernews"),
]
