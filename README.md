## 📌 Descripción del Proyecto

Este laboratorio tiene como objetivo el desarrollo de un formulario web que permite recolectar datos personales de manera **segura** y **validada** desde el lado del cliente. Utilizando HTML5, CSS3 y JavaScript, se implementaron técnicas de validación con **expresiones regulares**, **control de tipo**, **longitud** y **rango** para evitar el ingreso de datos inválidos o maliciosos.

---

## 🧪 Tecnologías Utilizadas

- HTML5
- CSS3 (diseño responsive)
- JavaScript (validaciones con RegEx)
---

![Uploading Captura de pantalla 2025-07-01 114623.png…]()

---

## 📄 Campos Validados

| Campo             | Validación                                                               |
|------------------|--------------------------------------------------------------------------|
| Nombre / Apellido| Solo letras, entre 3 y 30 caracteres                                     |
| Cédula / RUC     | Numérico, exactamente 10 (cédula) o 13 dígitos (RUC)                     |
| Teléfono         | 10 dígitos numéricos                                                     |
| Fecha Nacimiento | Entre 01/01/1900 y la fecha actual                                       |
| Género           | Campo obligatorio tipo select                                            |
| Dirección        | Máximo 20 caracteres, sin símbolos peligrosos                            |
| Salario          | Numérico entre $470 y $5000                                              |
| Email            | Estructura válida conforme al estándar de correos                        |
| Sitio Web        | URL válida que empiece con `http://` o `https://`                        |
| Contraseña       | De 8 a 12 caracteres, con mayúscula, minúscula, número y símbolo especial|

---

## ✅ Funcionalidades

- Validación en tiempo real con mensajes visuales (verde: válido / rojo: inválido).
- Prevención de envío de datos si existen errores en los campos.
- Mensaje general de éxito si el formulario se completa correctamente.
