from resources.user.auth import UserSignupApi,UserLoginApi
from resources.doctor.auth import DoctorLoginApi,DoctorSignupApi
def initialize_routes(api):
    api.add_resource(UserSignupApi, '/user/signup')
    api.add_resource(UserLoginApi, '/user/login')
    api.add_resource(DoctorSignupApi, '/doctor/signup')
    api.add_resource(DoctorLoginApi, '/doctor/login')