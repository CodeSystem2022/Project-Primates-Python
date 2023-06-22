class HealthPersonal:
    _id_counter = 0

    def __init__(self, name, surname, age, speciality, access_level,
                 email=None, phone=None, address=None, experience=None,
                 education=None, languages=None,
                 consultation_fee=None, availability=None):
        HealthPersonal._id_counter += 1
        self._personal_id = HealthPersonal._id_counter
        self._name = name  # Nombre del doctor o miembro del personal de salud.
        self._surname = surname  # Apellido del doctor o miembro del personal de salud.
        self._age = age  # Edad del doctor o miembro del personal de salud.
        self._speciality = speciality  # Especialidad médica del doctor o miembro del personal de salud.
        self._access_level = access_level  # Nivel de acceso o permisos del doctor o miembro del personal de salud.
        self._email = email  # Dirección de correo electrónico del doctor o miembro del personal de salud.*
        self._phone = phone  # Número de teléfono del doctor o miembro del personal de salud.*
        self._address = address  # Dirección del consultorio o lugar de trabajo del doctor.*
        self._experience = experience  # Experiencia laboral del doctor o miembro del personal de salud.*
        self._education = education  # Educación y formación académica del doctor o miembro del personal de salud.*
        self._languages = languages  # Idiomas que habla el doctor o miembro del personal de salud.*
        self._consultation_fee = consultation_fee  # Tarifa de consulta del doctor o miembro del personal de salud.*
        self._availability = availability  # Disponibilidad de citas del doctor o miembro del personal de salud.*
        # Los items con * al final son opcionales.

    # Métodos Getter.
    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def speciality(self):
        return self._speciality

    @property
    def access_level(self):
        return self._access_level

    @property
    def get_email(self):
        return self._email

    @property
    def get_phone(self):
        return self._phone

    @property
    def get_address(self):
        return self._address

    @property
    def get_experience(self):
        return self._experience

    @property
    def get_education(self):
        return self._education

    @property
    def get_languages(self):
        return self._languages

    @property
    def get_consultation_fee(self):
        return self._consultation_fee

    @property
    def get_availability(self):
        return self._availability

    # Métodos Setter.
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @speciality.setter
    def speciality(self, new_speciality):
        self._speciality = new_speciality

    @access_level.setter
    def access_level(self, new_access_level):
        self._access_level = new_access_level

    def __str__(self):
        return f'----------------------------------------------------------\n' \
               f'ID: {self._personal_id}\n' \
               f'Nombre: {self._name} {self._surname}, Edad: {self._age}\n' \
               f'Especialidad: {self._speciality}, Nivel de acceso: {self._access_level}\n' \
               f'Email: {self._email}\nTeléfono: {self._phone}\nDirección: {self._address}\n' \
               f'Experiencia: {self._experience} años\nEducación: {self._education}\n' \
               f'Idiomas: {self._languages}\nTarifa de consulta: ${self._consultation_fee}\n' \
               f'Disponibilidad: {self._availability}\n' \


# Parte de pruebas.


if __name__ == '__main__':
    doctor = HealthPersonal('Nico', 'Sgandurra', 21, 'Cirujano', 'High', 'Nico.Sg@gmail.com',
                            '2604667189', '3 De Febrero 880', 10,
                            'UNCuyo', ['English', 'Spanish'],
                            27000, 'Lunes a Jueves')

    print(doctor.age)  # Obtener el valor de age
    doctor.age = 35  # Establecer un nuevo valor para age

    print(doctor.speciality)  # Obtener el valor de speciality
    doctor.speciality = 'Cardiólogo'  # Establecer un nuevo valor para speciality

    print(doctor.access_level)  # Obtener el valor de access_level
    doctor.access_level = 'Medium'  # Establecer un nuevo valor para access_level

    print(doctor)

    # doctor2 = HealthPersonal('Nico', 'Sgandurra', 21, 'Cirujano', 'High') # Test de elementos opcionales
    # print(doctor2)
