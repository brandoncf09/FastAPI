from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"description": "No encontrado"}})

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4",
                 "Producto 5"
                 ]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]


# Hacer la divicion dentro de DOCS  entre cada uno de los productos