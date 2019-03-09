from django.urls import path
from . import views
from .views import (
                    PostListView,
                    PunchlineDetailView,
                    add_comment_to_punchline,
                    search,
                    )



urlpatterns=[

path('',PostListView.as_view(),name='post-home'),
path('search',views.search, name='search'),
path('punchline/<int:pk>/detail/', PunchlineDetailView.as_view(), name='punchline_detail'),

path('punchline/<int:pk>/comment/', views.add_comment_to_punchline, name='add_comment_to_punchline'),

]
