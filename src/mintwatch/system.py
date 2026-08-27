from pathlib import Path

def get_os_info() -> dict[str, str]:
    os_release = Path("/etc/os-release")

    info = {}

    for line in os_release.read_text().splitlines():
        key, value = line.split("=", 1)
        info[key] = value.strip('"')

    return info

def get_os_name() -> str:
    result = get_os_info()

    result["NAME"]