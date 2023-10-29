from django.urls import path
from .views import *

urlpatterns = [
    # ... other URL patterns ...
    path('groups/create', CreateGroupView.as_view(), name='create-group'),
    path('groups-list/', CreateGroupView.as_view(), name='list-group'),
    path('channel/create', CreateChannelView.as_view(), name='create-group'),
    path('video-channel/create', CreateVideoChannelView.as_view(), name='create-videochannel'),
    path('video-channels-list/<int:id>', GroupVideoChannelView.as_view(), name='vchennels-list'),
    path('user-groups/<int:user_id>', UserGroupsListView.as_view(), name='user-groups-list'),
    path('channels-list/<int:id>', GroupChannelView.as_view(), name='channels-list'),
    path('channel-previous-chat/<int:channel>', PreviousGroupMessagesView.as_view(), name='channels-chat'),
    path('group-details/<int:id>', GroupsDetailsView.as_view(), name='group-details'),
    path('channel-details/<int:id>', ChannelDetailsView.as_view(), name='channel-details'),
    path('group-members/', GroupMemberCreateView.as_view(), name='group-member-create'),

]