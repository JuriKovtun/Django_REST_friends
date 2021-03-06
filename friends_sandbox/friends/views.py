from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
# from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from friendship.models import Friend, FriendshipRequest

from friends_sandbox.friends.serializers import UserSerializer, GroupSerializer, FriendshipRequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FriendViewSet(viewsets.ViewSet):
    """
    ViewSet for Friend model
    """
    queryset = Friend.objects.all()


class FriendshipRequestViewSet(viewsets.ViewSet):
    """
    ViewSet for Friend model
    """
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer


# class FriendViewSet(viewsets.ViewSet):
#     """
#     ViewSet for Friend model
#     """

#     permission_classes = config.permission_classes
#     serializer_class = config.user_serializer

#     def list(self, request):
#         friends = Friend.objects.friends(request.user)
#         serializer = self.serializer_class(friends, many=True)
#         return Response(serializer.data)

#     @list_route()
#     def requests(self, request):
#         friend_requests = Friend.objects.unrejected_requests(user=request.user)
#         return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

#     @list_route()
#     def sent_requests(self, request):
#         friend_requests = Friend.objects.sent_requests(user=request.user)
#         return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

#     @list_route()
#     def rejected_requests(self, request):
#         friend_requests = Friend.objects.rejected_requests(user=request.user)
#         return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

#     def create(self, request):
#         """
#         Creates a friend request
#         POST data:
#         - user_id
#         - message
#         """

#         friend_obj = Friend.objects.add_friend(
#             request.user,                                                     # The sender
#             get_object_or_404(get_user_model(),
#                               pk=request.data['user_id']),  # The recipient
#             message=request.data.get('message', '')
#         )

#         return Response(
#             FriendshipRequestSerializer(friend_obj).data,
#             status.HTTP_201_CREATED
#         )

#     def destroy(self, request, pk=None):
#         """
#         Deletes a friend relationship
#         The user id specified in the URL will be removed from the current user's friends
#         """

#         user_friend = get_object_or_404(get_user_model(), pk=pk)

#         if Friend.objects.remove_friend(request.user, user_friend):
#             message = 'deleted'
#             status_code = status.HTTP_204_NO_CONTENT
#         else:
#             message = 'not deleted'
#             status_code = status.HTTP_304_NOT_MODIFIED

#         return Response(
#             {"message": message},
#             status=status_code
#         )


# class FriendshipRequestViewSet(viewsets.ViewSet):
#     """
#     ViewSet for FriendshipRequest model
#     """
#     permission_classes = config.permission_classes

#     @detail_route(methods=['post'])
#     def accept(self, request, pk=None):
#         friendship_request = get_object_or_404(
#             FriendshipRequest, pk=pk, to_user=request.user)
#         friendship_request.accept()
#         return Response(
#             FriendshipRequestSerializer(friendship_request).data,
#             status.HTTP_201_CREATED
#         )

#     @detail_route(methods=['post'])
#     def reject(self, request, pk=None):
#         friendship_request = get_object_or_404(
#             FriendshipRequest, pk=pk, to_user=request.user)
#         friendship_request.reject()
#         return Response(
#             FriendshipRequestSerializer(friendship_request).data,
#             status.HTTP_201_CREATED
#         )
