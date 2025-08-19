
from .models import Curso, Proyecto
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages



# Create your views here.

def home(request):

    return render(request, 'home.html')

def educacion(request):
    carrera1 = "Desarrollo de Software"
    universidad1 = "Instituto Tecnológico de las Américas (ITLA)"
    descripcion_carrera1 = (
        "La carrera de Desarrollo de Software forma profesionales altamente capacitados para diseñar,"
        "desarrollar, implementar y mantener aplicaciones y sistemas tecnológicos completos."
        "Los estudiantes adquieren conocimientos sólidos tanto en desarrollo backend —gestionando bases de datos,"
        "servidores y lógica de negocio— como en desarrollo frontend —creando interfaces intuitivas y atractivas para los usuarios—."
        "Además, se profundiza en metodologías ágiles, control de versiones, pruebas y despliegue de software,"
        "preparando a los egresados para afrontar los retos del mundo tecnológico actual y aportar soluciones innovadoras en múltiples industrias."
    )


    carrera2 = "Programa de Inglés por Inmersión"
    universidad2 = "Universidad Autónoma de Santo Domingo (UASD)"
    descripcion_carrera2 = "Enfoque del programa con metodología 100 por ciento en inglés, enfoque comunicativo y práctico. Logros específicos dominio certificado en habilidades de speaking y writing nivel B2 C1 MCER. Fluidez acelerada adquisición de competencias avanzadas en comprensión auditiva, expresión oral, lectura y escritura mediante metodologías interactivas clases 100 por ciento en inglés, debates, presentaciones y proyectos colaborativos. Enfoque profesional vocabulario técnico aplicado a mi área de estudio y trabajo como negocios, tecnología, educación, con simulaciones de entornos laborales internacionales."


    cursos = Curso.objects.all()  # Obtiene todos los cursos de la base de datos

    return render(request, 'educacion.html', {
        'carrera1': carrera1,
        'universidad1': universidad1,
        'descripcion_carrera1': descripcion_carrera1,
        'carrera2': carrera2,
        'universidad2': universidad2,
        'descripcion_carrera2': descripcion_carrera2,
        'cursos': cursos
    })

def proyecto(request):
    proyecto = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyecto})


def habilidad(request):
    
    return render(request, 'habilidades.html')




def contacto(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Mensaje de: {email}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Tu mensaje fue enviado correctamente ✅")
            return redirect("contacto")
        except Exception as e:
            messages.error(request, f"Ocurrió un error ❌: {e}")

    return render(request, "contacto.html")