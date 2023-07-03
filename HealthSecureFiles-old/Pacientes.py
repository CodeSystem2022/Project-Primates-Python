class Pacientes:
    _id_counter = 0

    def __init__(
            self, name, surname, age, previous_visits=None, future_visits=None, studies=None, report=None,
            address=None, phone_number=None, gender=None, date_of_birth=None, allergies=None,
            current_medications=None, family_medical_history=None, test_results=None, previous_procedures=None
    ):
        Pacientes._id_counter += 1
        self._paciente_id = Pacientes._id_counter
        self._name = name  # Nombre del paciente.
        self._surname = surname  # Apellido del paciente.
        self._age = age  # Edad del paciente.
        self._previous_visits = previous_visits  # Visitas anteriores del paciente al hospital.*
        self._future_visits = future_visits  # Visitas programadas del paciente al hospital en el futuro.*
        self._studies = studies  # Estudios realizados o en curso para el paciente.*
        self._report = report  # Informe actual del estado del paciente.*
        self._address = address  # Dirección del paciente.*
        self._phone_number = phone_number  # Número de teléfono del paciente.*
        self._gender = gender  # Género del paciente.*
        self._date_of_birth = date_of_birth  # Fecha de nacimiento del paciente.*
        self._allergies = allergies  # Alergias del paciente.*
        self._current_medications = current_medications  # Medicamentos actuales del paciente.*
        self._family_medical_history = family_medical_history  # Antecedentes médicos familiares del paciente.*
        self._test_results = test_results  # Resultados de pruebas médicas o de laboratorio del paciente.*
        self._previous_procedures = previous_procedures  # Procedimientos médicos anteriores del paciente.*
        # Los items con * al final son opcionales.

    @property
    def paciente_id(self):
        return self._paciente_id

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
    def previous_visits(self):
        return self._previous_visits

    @property
    def future_visits(self):
        return self._future_visits

    @property
    def studies(self):
        return self._studies

    @property
    def report(self):
        return self._report

    @property
    def address(self):
        return self._address

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def gender(self):
        return self._gender

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def allergies(self):
        return self._allergies

    @property
    def current_medications(self):
        return self._current_medications

    @property
    def family_medical_history(self):
        return self._family_medical_history

    @property
    def test_results(self):
        return self._test_results

    @property
    def previous_procedures(self):
        return self._previous_procedures

    # Method toString

    def __str__(self):
        return f"ID: {self.paciente_id}\n" \
               f'Nombre: {self._name} {self._surname}, Edad: {self._age}\n' \
               f"Visitas anteriores: {self.previous_visits}\n" \
               f"Visitas futuras: {self.future_visits}\n" \
               f"Estudios: {self.studies}\n" \
               f"Informe: {self.report}\n" \
               f"Dirección: {self.address}\n" \
               f"Número de teléfono: {self.phone_number}\n" \
               f"Género: {self.gender}\n" \
               f"Fecha de nacimiento: {self.date_of_birth}\n" \
               f"Alergias: {self.allergies}\n" \
               f"Medicamentos actuales: {self.current_medications}\n" \
               f"Antecedentes médicos familiares: {self.family_medical_history}\n" \
               f"Resultados de pruebas: {self.test_results}\n" \
               f"Procedimientos anteriores: {self.previous_procedures}"


if __name__ == '__main__':
    paciente = Pacientes(
        name="Nico",
        surname="Sgandurra",
        age=21,
        previous_visits=["2021-01-10", "2022-05-20"],
        future_visits=["2023-07-15", "2023-12-30"],
        studies=["Radiografía", "Tomografía computada"],
        report="Buen estado de salud general",
        address="3 De Febrero 880",
        phone_number="2604617188",
        gender="Masculino",
        date_of_birth="05-09-2001",
        allergies=["Sandía", "Penicilina"],
        current_medications="Ibupirac",
        family_medical_history="Asma",
        test_results="Adecuados",
        previous_procedures="Cirugía por fractura"
    )
    print(paciente)
