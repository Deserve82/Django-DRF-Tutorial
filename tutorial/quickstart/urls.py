from django.urls import path
from .views import PollView, ChoiceList, CreateVote, UserCreate, LoginView, PostView, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollView, base_name='polls')
router.register('posts', PostView, base_name='posts')
router.register('user', UserView, base_name='users')
urlpatterns = [
    path("polls/<int:pk>/choices", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login")
]
urlpatterns += router.urls
