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

def get_uptime() -> str:
    os_uptime = Path("/proc/uptime")

    uptime_seconds = float(os_uptime.read_text().split(" ")[0])

    hours = int(uptime_seconds // 3600)
    remaining_seconds = uptime_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)

    return f"{hours}h {minutes}m {seconds}s"