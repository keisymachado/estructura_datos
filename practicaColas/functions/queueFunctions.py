from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """

    opciones = { 
        "duda",
        "caja",
        "asesor",
        "otros"
    }

    if ticket.type not in opciones:
        print ( "invalid action type")
        return
    
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController()

    ticketTypes[ticket.type].enqueue(ticket)    
    print(f"Ticket de tipo '{ticket.type}' Añadido a la cola")
