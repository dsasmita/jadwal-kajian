from rest_framework import serializers, relations

from kajian.models import Schedule, City, Province, Mosque, Ustad


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:schedule-detail")
    city = relations.HyperlinkedRelatedField(
        view_name="api:city-detail", queryset=City.objects.all(),
    )
    mosque = relations.HyperlinkedRelatedField(
        view_name="api:mosque-detail", queryset=Mosque.objects.all(),
    )
    ustad = relations.HyperlinkedRelatedField(
        many=True,
        view_name="api:ustad-detail", queryset=Ustad.objects.all(),
    )

    class Meta:
        model = Schedule
        fields = '__all__'

class MosqueSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:mosque-detail")
    city = relations.HyperlinkedRelatedField(
        view_name="api:city-detail", queryset=City.objects.all(),
    )

    class Meta:
        model = Mosque
        fields = '__all__'

class CitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:city-detail")
    province = relations.HyperlinkedRelatedField(
        view_name="api:province-detail", queryset=Province.objects.all(),
    )

    class Meta:
        model = City
        fields = '__all__'

class UstadSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:ustad-detail")

    class Meta:
        model = Ustad
        fields = '__all__'

class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:province-detail")

    class Meta:
        model = Province
        fields = '__all__'