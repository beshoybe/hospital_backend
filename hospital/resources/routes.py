from resources.user.auth import UserSignupApi,UserLoginApi
from resources.doctor.auth import DoctorLoginApi,DoctorSignupApi
from resources.report.report import AddReportApi,AddUserReportApi
from resources.radiology.radiology import AddRadiologyApi,AddRadiologyImageApi,AddUserRadiologyApi
def initialize_routes(api):
    api.add_resource(UserSignupApi, '/user/signup')
    api.add_resource(UserLoginApi, '/user/login')
    api.add_resource(DoctorSignupApi, '/doctor/signup')
    api.add_resource(DoctorLoginApi, '/doctor/login')
    api.add_resource(AddReportApi, '/doctor/report')
    api.add_resource(AddRadiologyApi, '/doctor/radiology')
    api.add_resource(AddRadiologyImageApi, '/doctor/radiology/image')
    api.add_resource(AddUserReportApi, '/user/report')
    api.add_resource(AddUserRadiologyApi, '/user/radiology')
    