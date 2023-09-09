from .core import QRCodeServiceContext, AuthorizedQRCodeService
from fastapi.params import Header, Depends
from .models import User
from fastapi import APIRouter


def AuthorizedQRCodeServiceRouter(authorized_admin_service: AuthorizedQRCodeService):
    router = APIRouter(prefix='/qrcode')

    async def context_():
        return authorized_admin_service.context()

    @router.post("/create_file")
    async def create_user(user: User, context: QRCodeServiceContext = Depends(context_)):
        return context.create_user(user=user)

    @router.get("/get_file")
    async def get_file(file_uuid: str, context: QRCodeServiceContext = Depends(context_)):
        return context.get_file(file_uuid=file_uuid)

    return router
