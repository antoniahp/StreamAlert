import uuid

from django.db import models

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    provider_id= models.UUIDField()
    image = models.URLField()
    date = models.DateTimeField()
    category = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_category(self) -> str:
        category_mapper = {
            "0": "Funko",
            "1": "Cartas Pokemon",
            "2": "Figuras",
            "3": "Videojuegos",
            "4": "Lego",
            "5": "Street Wear",
            "6": "Ropa Vintage",
            "7": "Deportivas",
            "8": "Cartas One Piece",
            "9": "Carats Magic",
            "10": "Cartas Yu-Gi-Oh!",
            "11": "Cartas Futbol",
            "12": "Cartas Balonceto",
            "13": "Música",
            "14": "Cómics",
            "15": "Libros",
            "16": "Películas",
            "17": "Bolsos",
            "18": "Accesorios",
            "19": "Zapatos"
        }

        return category_mapper.get(self.category, "Varios")