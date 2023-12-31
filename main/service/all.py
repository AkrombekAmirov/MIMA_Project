from ..repositories import user_repository, file_repository
from ..config import secret_key, algorithm, expire_time
# from admin_service.core import AdminService
from auth_service.core import AuthService
from token_manager import TokenManager
from QR_code_service.core import QRCodeService

token_manager = TokenManager(secret=secret_key, algorithm=algorithm, expire_time=expire_time,
                             user_repository=user_repository)
auth_service = AuthService(user_repository=user_repository, token_manager=token_manager)
qrcode_service = QRCodeService(user_repository=user_repository, file_repository=file_repository)

# register_service = RegisterService(patient_repository=patient_repository, user_repository=user_repository,
#                                    file_repository=file_repository)
# doctor_service = DoktorService(patient_repository=patient_repository, user_repository=user_repository,
#                                file_repository=file_repository)
# admin_service = AdminService(user_repository=user_repository, patient_repository=patient_repository)