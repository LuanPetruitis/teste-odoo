from app.models.product import ProductEditModel, ProductModel
from app.service.product import Product
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/product", tags=["Produtos"])


product_service = Product()


@router.post("/create")
def create_product(data_product: ProductModel):
    """
    Caso não envie o ID ele é calculado automáticamente
    """
    product_created = product_service.create(data_product.dict())
    if not product_created:
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Já existe um produto com esse nome."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder({"message": "Produto criado com sucesso!"}),
        status_code=status.HTTP_201_CREATED,
    )


@router.put("/edit")
def delete_product(product_id: str, data_product: ProductEditModel):
    product_deleted = product_service.edit(product_id, data_product.dict())
    if not product_deleted:
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": "Produto não foi editado com sucesso, já existe um produto com esse nome."
                }
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder({"message": "Produto editado com sucesso!"}),
        status_code=status.HTTP_200_OK,
    )


@router.delete("/delete")
def delete_product(product_id: str):
    product_deleted = product_service.delete(product_id)
    if not product_deleted:
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Produto não foi removido com sucesso!"}
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder({"message": "Produto removido com sucesso!"}),
        status_code=status.HTTP_200_OK,
    )


@router.get("/find_product")
def find_product(product_id: str):
    product = product_service.find(product_id)
    if not product:
        return JSONResponse(
            content=jsonable_encoder({"message": "Produto não foi encontrado!"}),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(product),
        status_code=status.HTTP_200_OK,
    )


@router.get("/all_products")
def all_products():
    products = product_service.all_products()
    if not products:
        return JSONResponse(
            content=jsonable_encoder({"message": "Produtos não foram encontrados!"}),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(products),
        status_code=status.HTTP_200_OK,
    )
