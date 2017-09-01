configs = {
    'HostIP': '10.203.106.250',
    'Server': '10.203.106.250',
    'ServerPort': 8000,
    'urls': {
        'get_configs': ['monitor/api/client/config', 'get'],
        'service_report': ['monitor/api/client/service/report/', 'post'],
    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300,
}
