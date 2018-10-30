from rest_framework import serializers;
from .models import Language,Paradigm,Programmer;
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Language;
        fields='__all__';
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Paradigm;
        fields='__all__';
class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Programmer;
        fields='__all__';
