import pytest

from canyon_notifier.bike import Bike


@pytest.mark.parametrize(
    "test_name, bike_name, bike_url, bike_size, expected_availability",
    [
        (
            'bike-available',
            'Grail CF SLX 8 Di2',
            'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/cf-slx/grail-cf-slx-8-di2/3099.html?dwvar_3099_pv_rahmenfarbe=R061_P08',
            'S',
            True
        ),
        (
            'bike-not-available',
            'Grail 6 Al - forest',
            'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/al/grail-6/3092.html?dwvar_3092_pv_rahmenfarbe=GN%2FBK',
            'XL',
            False
        )

    ]
)
def test_parser(test_name, bike_name, bike_url, bike_size, expected_availability):
    bike = Bike(
        name=bike_name,
        link=bike_url,
        size=bike_size
    )

    bike.update()

    assert bike.avail == expected_availability