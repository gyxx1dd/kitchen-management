from kitchen.models import Reservation


def if_table_available(table, date, time_start, time_end):
    reservations = Reservation.objects.filter(table=table)

    for reservation in reservations:
        if reservation.date == date:
            if reservation.date == date:
                if (
                        reservation.time_start < time_end
                        and reservation.time_end > time_start
                ):
                    return False
    return True