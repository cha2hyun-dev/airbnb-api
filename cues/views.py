from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cue
from .serializers import CueSerializer


class CuesView(APIView):
    def get(self, request):
        cues = Cue.objects.all()
        serializer = CueSerializer(cues,many=True).data
        return Response(serializer)
    
    def post(self, request):
        serializer = CueSerializer(data=request.data)
        if serializer.is_valid():
            cue = serializer.save()
            cue_serializer = CueSerializer(cue).data
            return Response(data=cue_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def get(self, request):
    #     rooms = Room.objects.all()[:5]
    #     serializer = CueSerializer(rooms, many=True).data
    #     return Response(serializer)

    # def post(self, request):
    #     if not request.user.is_authenticated:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)
    #     serializer = CueSerializer(data=request.data)
    #     if serializer.is_valid():
    #         room = serializer.save(user=request.user)
    #         room_serializer = CueSerializer(room).data
    #         return Response(data=room_serializer, status=status.HTTP_200_OK)
    #     else:
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CueView(APIView):
    pass
    # def get_room(self, pk):
    #     try:
    #         room = Room.objects.get(pk=pk)
    #         return room
    #     except Room.DoesNotExist:
    #         return None

    # def get(self, request, pk):
    #     room = self.get_room(pk)
    #     if room is not None:
    #         serializer = CueSerializer(room).data
    #         return Response(serializer)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, pk):
    #     room = self.get_room(pk)
    #     if room is not None:
    #         if room.user != request.user:
    #             return Response(status=status.HTTP_403_FORBIDDEN)
    #         serializer = CueSerializer(room, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             room = serializer.save()
    #             return Response(CueSerializer(room).data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         return Response()
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def delete(self, request, pk):
    #     room = self.get_room(pk)
    #     if room is not None:
    #         if room.user != request.user:
    #             return Response(status=status.HTTP_403_FORBIDDEN)
    #         room.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    