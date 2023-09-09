from user_repository import UserRepository, User
from fastapi.responses import StreamingResponse
from file_repository import FileService
from auth_service import AuthService
from gzip import compress, decompress
from uuid import uuid4


class QRCodeService:
    def __init__(self,
                 user_repository: UserRepository,
                 file_repository: FileService
                 ):
        self.user_repository = user_repository
        self.file_repository = file_repository

    def context(self, user):
        # if user.role != "admin": raise Exception("incorrect role")
        return QRCodeServiceContext(self, user)


class AuthorizedQRCodeService:
    def __init__(self, qr_code_service: QRCodeService, auth_service: AuthService):
        self.qr_code_service = qr_code_service
        self.auth_service = auth_service

    def context(self):
        # return self.qr_code_service.context(self.auth_service.retrieve_user(token))
        return True


class QRCodeServiceContext:
    def __init__(self, qrcode: QRCodeService, QRcode) -> None:
        self.service = qrcode
        self.QRcode = QRcode

    def create_user(self, user):
        return self.service.user_repository.create_user(User(**user.dict())).id

    def get_user(self, user_id: int):
        return self.service.user_repository.get_user(id=user_id)

    def get_users(self):
        return self.service.user_repository.get_users()

    def create_file(self, user_id: int, image: bytes, content_type: str):
        uuid = str(uuid4())
        self.service.file_repository.create_file_chunk(image=image, file_uuid=uuid)
        return self.service.file_repository.create_file(user_id=user_id, file_uuid=uuid, content_type=content_type)

    def get_file(self, file_uuid: str):
        def iterfile():
            yield decompress(b"".join(
                [element.chunk for element in self.service.file_repository.get_file(file_id=file_uuid)]))

        return StreamingResponse(iterfile(), media_type=self.service.file_repository.get_file_(
            file_uuid=file_uuid).content_type)
