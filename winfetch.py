import os  # !Import necessary libraries
import platform
import socket
import psutil
import GPUtil
import cpuinfo
import time
import locale
from colorama import Fore, init

# Needed for Windows terminal colors to work
init(autoreset=True)

# function to grab the osinfo using platform


def os_info():
    system = platform.system()
    release = platform.release()
    version = platform.version()
    return f"{Fore.LIGHTRED_EX}OS: {Fore.RESET}{system} {release} {version}"

# function to grab the username using os


def user_info():
    username = os.getlogin()
    return f"{Fore.LIGHTRED_EX}USER: {Fore.RESET}{username}"

# function to grab the system cpu using cpuinfo


def cpu_info():
    cpu_info = cpuinfo.get_cpu_info()
    cpu_name = cpu_info['brand_raw']
    cpu_cores = psutil.cpu_count(logical=False)  # Get physical core count
    return f"{Fore.LIGHTRED_EX}CPU: {Fore.RESET}{cpu_name} {cpu_cores} Cores"

# function to grab the system memory using psutil


def memory_info():
    memory = psutil.virtual_memory()
    used_memory = memory.used >> 20  # Convert to MiB
    total_memory = memory.total >> 20  # Convert to MiB
    return f"{Fore.LIGHTRED_EX}Memory: {Fore.RESET}{used_memory}MiB / {total_memory}MiB"

# function to grab the system hostname using socket


def hostname():
    host = socket.gethostname()
    return f"{Fore.LIGHTRED_EX}HOSTNAME: {Fore.RESET}{host}"

# function to grab the system architecture using platform


def system_architecture():
    arch = platform.architecture()[0]
    return f"{Fore.LIGHTRED_EX}Architecture: {Fore.RESET}{arch}"

# function to grab the system uptime using psutil


def system_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60
    return f"{Fore.LIGHTRED_EX}Uptime: {Fore.RESET}{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# function to grab the system time using time


def system_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return f"{Fore.LIGHTRED_EX}System Time: {Fore.RESET}{current_time}"

# function to grab system locale using locale


def system_locale():
    user_locale = locale.getlocale()
    language, region = user_locale
    return f"{Fore.LIGHTRED_EX}System Locale: {Fore.RESET}{language} ({region})"

# function to grab gpu info using GPUtil


def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return "No GPUs found."
        gpu_info = []
        for gpu in gpus:
            gpu_info.append(f"{Fore.LIGHTRED_EX}GPU: {Fore.RESET}{
                            gpu.name} {gpu.driver} {gpu.memoryTotal} MB")
        return " | ".join(gpu_info)
    except Exception as e:
        return str(e)


def ascii_logo():
    logo = f"""
                            ********
            *** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************

*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
*************** ********************
            *** ********************
                           *********
"""
    return logo

# * This function is so the logo appears on the left and the info on the right


def display_info(ascii_art, system_info):
    ascii_lines = ascii_art.split('\n')
    info_lines = system_info.split('\n')
    max_lines = max(len(ascii_lines), len(info_lines))

    output = []

    for i in range(max_lines):
        ascii_line = ascii_lines[i] if i < len(ascii_lines) else ''
        info_line = info_lines[i] if i < len(info_lines) else ''

        output.append(f"{ascii_line.ljust(50)} {info_line}")

    return '\n'.join(output)


gpu_information = get_gpu_info()
ascii_art = ascii_logo()
# Compile system information
system_information = "\n".join(
    [os_info(), user_info(), hostname(), cpu_info(), memory_info(), system_architecture(), system_time(), system_locale(), system_uptime(), gpu_information])

# Show the compiled system info with the ascii logo
output = display_info(ascii_art, system_information)
print(output)
