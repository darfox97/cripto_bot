import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


def create_mail(coin_data, recipients):
    apiemail = os.environ.get("SENDGRID_EMAIL")

    # Genera las filas de la tabla dinámicamente
    table_rows = ""
    for coin in coin_data:
        table_rows += f"""
            <tr>
                <td>{coin[1]}</td>
                <td>{coin[3]}</td>
                <td>{coin[4]}</td>
            </tr>
        """

    message = Mail(
        from_email=apiemail,
        to_emails=recipients,
        subject="Reporte diario criptomonedas.",
        html_content=f"""
            <h1>Reporte Cripto:</h1>
            <h2> Fecha: {coin_data[0][0]} </h2>
            <table>
                <tr>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Variación</th>
                </tr>
                {table_rows}
            </table>
            <footer>Enviado con Sendgrid para la prácticas de Plexus.</footer>"""
    )
    return message


def send_email(message):
    apikey = os.environ.get("SENDGRID_API_KEY")
    try:
        sg = SendGridAPIClient(apikey)
        response = sg.send(message)
        print(response.status_code, response.body, response.headers)
    except Exception as ex:
        print("Error al enviar.")
        print(ex)
