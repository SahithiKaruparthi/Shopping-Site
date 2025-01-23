from products import dao
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    description: str
    cost: float
    qty: int = 0

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(**data)


def list_products() -> list[Product]:
    """Fetch and return a list of all products as Product objects."""
    return [Product.from_dict(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetch and return a single product by its ID."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.from_dict(product_data)


def add_product(product_data: dict):
    """Add a new product to the database."""
    if not all(key in product_data for key in ["id", "name", "description", "cost", "qty"]):
        raise ValueError("Missing required product fields.")
    dao.add_product(product_data)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a specific product."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    if not dao.get_product(product_id):
        raise ValueError(f"Product with ID {product_id} not found.")
    dao.update_qty(product_id, qty)
