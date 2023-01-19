"""View module for handling requests about menu items"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from brianscafeapi.models import MenuItem

class MenuItemView(ViewSet):
    """Brian's Cafe menu items view"""
    
    def retrieve(self,request,pk):
        """Handle GET requests for a single menu item 
        
        Returns:
            Response -- JSON serialized menu item 
        """
        try:
            menu_item = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data)
        except MenuItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self,request):
        """Handle GET requests for all menu items
        
        Returns: 
            Response -- JSON serialized list of menu items
        """
        menu_item = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_item, many=True)
        return Response(serializer.data)
        
class MenuItemSerializer(serializers.ModelSerializer):
    """JSON serializer for menu items
    """
    class Meta:
        model = MenuItem
        fields = (
            'id',
            'name',
            'heat_level',
            'about',
            'cost'
        )