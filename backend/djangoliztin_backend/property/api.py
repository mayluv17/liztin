from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Property
from .serializers import PropertiesListSerializer, PropertiesDetailSerializer
from .forms import PropertyForm


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])

def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])

def properties_detail(request, pk):
    properties = Property.objects.get(pk=pk)
    serializer = PropertiesDetailSerializer(properties, many=False)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['POST', 'FILES'])
def create_property(request):
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():

            property = form.save(commit=False)
            property.landlord = request.user
            property.save()

            return JsonResponse({'success': True})

        else:
            print('error', form.errors, form.none_field_errors)
            return JsonResponse({'errors': form.errors.as_json()}, status=400)

