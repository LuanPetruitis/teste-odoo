from app.models.shopping_cart import ItemCart, ItensCartModel
from app.service.order import Order
from app.service.shopping_cart import ShoppingCart
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/shopping_cart", tags=["Carrinho"])


shopping_cart_service = ShoppingCart()
order_service = Order()


@router.post("/add_product")
def add_product(user_id: str, data: ItensCartModel):
    """
    user_id: str - A aplicação não possui usuário pois é uma aplicação simples porém em uma situação real o carrinho estaria relacionado ao usuário sendo um carrinho por usuário
    """
    product_added = shopping_cart_service.add_product(user_id, data.dict())
    if not product_added:
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Erro ao adicionar o produto no carrinho."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(
            {"message": "Produto adicionado ao carrinho com sucesso!"}
        ),
        status_code=status.HTTP_201_CREATED,
    )


@router.delete("/remover_product")
def remove_product(product_id: str, user_id: str):
    produtc_removed = shopping_cart_service.remove_product(product_id, user_id)
    if not produtc_removed:
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Erro ao remover produto do carrinho."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(
            {"message": "Produto removido do carrinho com sucesso!"}
        ),
        status_code=status.HTTP_200_OK,
    )


@router.patch("/edit_quantity_product")
def edit_quantity_product(user_id: str, data: ItemCart):
    produtc_edited = shopping_cart_service.edit_quantity_product(user_id, data.dict())
    if not produtc_edited:
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Erro ao editar a quantidade do produto no carrinho."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(
            {"message": "Quantidade do produto editada com sucesso!"}
        ),
        status_code=status.HTTP_200_OK,
    )


@router.get("/see")
def see_cart(user_id: str):
    return JSONResponse(
        content=jsonable_encoder(shopping_cart_service.find_cart(user_id)),
        status_code=status.HTTP_200_OK,
    )


@router.post("/finalize_order")
def finalize_order(user_id: str):
    # Criar order e apagar carrinho
    order = order_service.create(user_id)
    if not order:
        return JSONResponse(
            content=jsonable_encoder({"message": "Finalizar Pedido."}),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(order),
        status_code=status.HTTP_200_OK,
    )
