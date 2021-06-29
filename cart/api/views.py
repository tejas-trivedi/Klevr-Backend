


class CartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    @staticmethod
    def get_product(obj):
        return obj.product.name


class CartItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    item_title = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            "item",
            "item_title",
            "price",
            "product",
            "quantity",
            "line_item_total",
        ]
