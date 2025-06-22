from typing import cast
from random_user_agent.params import OperatingSystem, SoftwareName
from random_user_agent.user_agent import UserAgent

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.LINUX.value]


def _generate_random_user_agent() -> str:
    """
    Generate a random user agent string.

    Returns:
        str: A random user agent string.
    """
    # Create a UserAgent instance with specified software names and operating systems.
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100
    )

    # Get a random user agent string.
    return cast(str, user_agent_rotator.get_random_user_agent())


def generate_headers() -> dict[str, str]:
    """
    Generate headers with a random user agent.

    Returns:
        dict[str, str]: Headers containing a random user agent.
    """
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "pl;q=0.8",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://www.google.com/",
        "upgrade-insecure-requests": "1",
    }

    return headers | {"user-agent": _generate_random_user_agent()}
