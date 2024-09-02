# Propuesta de valor
Al explorar la plataforma de Geek, noté que no recibía notificaciones sobre los directos en curso, lo que me llevó a concebir este proyecto. Observé que en Chollometro utilizaban un canal de Telegram con gran éxito, lo que me inspiró a implementar una solución similar. Pensé que sería útil enviar un mensaje a los usuarios 30 minutos antes de cada transmisión en vivo, asegurando así que incluso los usuarios más despistados no se pierdan ningún directo.

Este repositorio contiene una integración entre la plataforma Geek.live y Telegram, diseñada para notificar a los usuarios de Geek 30 minutos antes de sus transmisiones en vivo. El proyecto se divide en dos partes principales:
## Importación de eventos:
Esta parte utiliza la API pública de Geek para obtener información sobre los eventos programados. Para automatizar este proceso, hemos desarrollado un comando personalizado en Django que se ejecuta cada hora. Este comando realiza una solicitud GET a la API, extrae los datos y los convierte al formato utilizado por nuestra aplicación, utilizando un importador específico que he creado. Durante este proceso, verificamos si el evento ya está registrado en nuestra base de datos, utilizando el provider_id (un UUID asociado a la URL del evento). Si el evento no está guardado en nuestra base de datos, se crea un nuevo registro y se guarda en la base de datos.

![admin](https://github.com/user-attachments/assets/93af35bb-b68d-4689-bf45-198a235117b1)

## Notificación de eventos:
Esta parte se encarga de notificar automáticamente a los usuarios 30 minutos antes de cada transmisión en vivo. Para ello, se realiza una consulta a la base de datos solicitando los eventos que ocurrirán dentro del rango de tiempo especificado (filtrados por date__gte y date__lte). Por cada evento que se encuentre en ese rango, se envía un mensaje de notificación a Telegram. Este proceso está automatizado mediante un comando personalizado en Django que, con la integración de crontab, se ejecuta cada 30 minutos para revisar los eventos próximos y enviar las notificaciones correspondientes.

<div align="center">
  <img src="https://github.com/user-attachments/assets/58aef664-23b6-4aa5-ae9d-54b7c7f44bad" width="250" height="500" alt="telegram">
</div>

## Pendiente / a mejorar:
1. Añadir tests unitarios y de integración.



## Resultado
https://github.com/user-attachments/assets/c0baebc9-4fc0-4c6e-930c-9e4f83560d75




