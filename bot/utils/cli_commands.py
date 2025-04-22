import re
import subprocess

from decouple import config


def get_raspberry_cpu_temp() -> str:
    """Get CPU temperature if it runs on RaspberryPi OS."""
    try:
        temp = subprocess.run(['vcgencmd', 'measure_temp'],
                              capture_output=True, text=True)
        return temp.stdout
    except FileNotFoundError:
        return "Seems like i'm not in Raspberry Pi..."


def get_logs(lines: int | None = None) -> str:
    '''Выполняет bash-команду `tail` для получения последних строчек файла с
    логами бота и возвращает строку, состоящую из потоков stderr и stdout
    выполненной команды. Количество выводимых строк задаётся параметром `lines`.
    Если параметр не задан или явно указан как `None`, то возвращается
    количество по умолчанию - 10 строк (определено в используемой утилите
    `tail`). Если в логах присутствует какой-либо id, заданный подстрокой
    'id=...', то все цифры id заменяются символами `*`.'''

    command = ['tail', config('LOGFILENAME')]
    if lines:
        command.insert(1, f'-{lines}')

    bash_stdout = subprocess.run(command, capture_output=True, text=True)
    logs = bash_stdout.stdout.strip()

    ids = set(re.findall(r'id=\d*', logs))
    for id in ids:
        id = id.replace('id=', '')
        logs = logs.replace(id, '*' * len(id))

    return bash_stdout.stderr + logs
