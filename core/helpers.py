import pytz
from babel.dates import format_datetime


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clear_layout(layout)


def format_date(datetime):
    return format_datetime(
        datetime=datetime,
        format='medium',
        locale='pt_BR',
        tzinfo=pytz.timezone('America/Manaus')
    )
