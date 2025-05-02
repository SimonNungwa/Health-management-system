from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

# Public Pages
@routes.route('/')
def index():
    return render_template('index.jinja')

@routes.route('/about')
def about():
    return render_template('public/about.jinja')

@routes.route('/contact')
def contact():
    return render_template('public/contact.jinja')

@routes.route('/faq')
def faq():
    return render_template('public/faq.jinja')

# Authentication
@routes.route('/login')
def login():
    return render_template('auth/login.jinja')

@routes.route('/signup')
def signup():
    return render_template('auth/signup.jinja')

@routes.route('/recover-password')
def recover_password():
    return render_template('auth/recoverpassword.jinja')

@routes.route('/user/dashboard')
def user_dashboard():
    return render_template('auth/userdashboard.jinja')

# Patient Pages
@routes.route('/patient/dashboard')
def patient_dashboard():
    return render_template('patient/patientdashboard.jinja')

@routes.route('/patient/book-appointment')
def book_appointment():
    return render_template('patient/bookappointment.jinja')

@routes.route('/patient/appointments')
def appointment_history():
    return render_template('patient/appointmenthistory.jinja')

@routes.route('/patient/medical-records')
def medical_records():
    return render_template('patient/medicalrecords.jinja')

@routes.route('/patient/prescriptions')
def prescriptions():
    return render_template('patient/prescriptions.jinja')

@routes.route('/patient/payments')
def payments():
    return render_template('patient/payments.jinja')

@routes.route('/patient/profile-settings')
def profile_settings():
    return render_template('patient/profilesettings.jinja')

@routes.route('/patient/telemedicine')
def telemedicine():
    return render_template('patient/telemedecine.jinja')

# Doctor Pages
@routes.route('/doctor/dashboard')
def doctor_dashboard():
    return render_template('doctor/doctordashboard.jinja')

@routes.route('/doctor/appointments')
def doctor_appointments():
    return render_template('doctor/appointmentmanager.jinja')

@routes.route('/doctor/patients')
def patient_list():
    return render_template('doctor/patientlist.jinja')

@routes.route('/doctor/notes')
def medical_notes():
    return render_template('doctor/medicalnotes.jinja')

@routes.route('/doctor/prescribe')
def prescribe():
    return render_template('doctor/prescribe.jinja')

@routes.route('/doctor/schedule')
def doctor_schedule():
    return render_template('doctor/schedulemanagement.jinja')

@routes.route('/doctor/settings')
def doctor_settings():
    return render_template('doctor/doctorsettings.jinja')

# Admin Pages
@routes.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.jinja')

@routes.route('/admin/analytics')
def analytics():
    return render_template('admin/analytics.jinja')

@routes.route('/admin/appointments')
def appointment_oversight():
    return render_template('admin/appointmentoversight.jinja')

@routes.route('/admin/payments')
def admin_payments():
    return render_template('admin/paymentcontrol.jinja')

@routes.route('/admin/settings')
def system_settings():
    return render_template('admin/systemsettings.jinja')

@routes.route('/admin/users')
def user_management():
    return render_template('admin/usermanagement.jinja')
