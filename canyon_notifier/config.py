import logging
import os

from canyon_notifier.bike import Bike

PREFIX = 'CANYON_BIKE_'

token = os.getenv('TOKEN')

interval = 60
log_level = logging.DEBUG

bike_map = []
for bike_id in range(10):
    if f'{PREFIX}{bike_id}' not in os.environ:
        break

    bike_map.append(
        Bike(
            name=os.environ.get(f'{PREFIX}{bike_id}'),
            link=os.environ.get(f'{PREFIX}{bike_id}_URL'),
            size=os.environ.get(f'{PREFIX}{bike_id}_SIZE'),
        )
    )

if not bike_map:
    raise RuntimeError('no bikes requested to check')
