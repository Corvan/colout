traceback_header = ["^Traceback .*$", "blue"]
file_line_in = [
    r'^\s{4}(File ")(/*.*?/)*([^/:]+)(", line) (\d+)(, in) (.*)$',
    "blue,  none,  white,blue,  yellow,blue",
    "normal,normal,bold, normal,normal,bold",
]
error_name = [r"^([A-Za-z]*Error):*", "red", "bold"]
exception_name = [r"^([A-Za-z]*Exception):*", "red", "bold"]
quoted_errors = [r"Error.*['\"](.*)['\"]", "magenta"]
python_code = [r"^\s{4}.*$", "Python", "monokai"]
log_levels = [
    [r"ERROR", "red"],
    [r"CRITICAL", "red", "bold"],
    [r"WARNING", "yellow"],
    [r"INFO", "cyan"],
    [r"DEBUG", "green"],
]
timestamp = [r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{1,7})", "purple"]
ip_addresses = [
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(:\d{1,5})?|"
    r"- ([0-9a-fA-F]{1,4}:{1,2}){1,7}([0-9a-fA-F]{1,4})",
    "orange",
]


def theme(context):
    return context, [
        traceback_header,
        file_line_in,
        error_name,
        exception_name,
        quoted_errors,
        python_code,
        *log_levels,
        timestamp,
        ip_addresses,
    ]
