from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ListModelView(APIView):
    model = None
    model_serializer = None

    def get(self, request, format=None):
        objects = self.model.objects.all()
        serializer = self.model_serializer(objects, many=True)
        return Response(serializer.data)


class CreateModelView(APIView):
    model = None
    model_serializer = None

    def post(self, request, format=None):
        serializer = self.model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailModelView(APIView):
    model = None
    model_serializer = None

    def _fetch_from_db(self, request, model_id):
        try:
            return self.model.objects.get(pk=model_id)
        except self.model.DoesNotExist:
            return None

    def get(self, request, model_id, format=None):
        obj = self._fetch_from_db(request, model_id)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.model_serializer(obj)
        return Response(serializer.data)

    def put(self, request, model_id, format=None):
        obj = self._fetch_from_db(request, model_id)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.model_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, model_id, format=None):
        obj = self._fetch_from_db(request, model_id)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
