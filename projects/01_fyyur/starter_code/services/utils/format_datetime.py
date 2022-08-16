import babel
import dateutil.parser


def format_datetime(value, format='medium'):
    date = None
    try:
        # Todo: Remove once all the data is fetched from the database
        date = dateutil.parser.parse(value)
    except:
        date = value

    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')

