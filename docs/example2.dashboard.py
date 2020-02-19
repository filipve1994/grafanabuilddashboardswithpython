from src.core import *
from src.prometheus import *
import src._gen

print("dashboardglobal: ", src._gen.dashboardvar)
print("environmentglobal: ", src._gen.environmentvar)

environment = src._gen.environmentvar
instance = src._gen.instancevar
# job = src._gen.job
job = 'upmviziworks-backend-application'

g1 = Graph(
    title="Frontend QPS",
    dataSource='prometheus',
    targets=[
        Target(
            expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"1.."}[1m]))',
            legendFormat="1xx",
            refId='A',
        ),
        Target(
            expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"2.."}[1m]))',
            legendFormat="2xx",
            refId='B',
        ),
        Target(
            expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"3.."}[1m]))',
            legendFormat="3xx",
            refId='C',
        ),
        Target(
            expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"4.."}[1m]))',
            legendFormat="4xx",
            refId='D',
        ),
        Target(
            expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"5.."}[1m]))',
            legendFormat="5xx",
            refId='E',
        ),
    ],
    yAxes=YAxes(
        YAxis(format=OPS_FORMAT),
        YAxis(format=SHORT_FORMAT),
    ),
    alert=Alert(
        name="Too many 500s on Nginx",
        message="More than 5 QPS of 500s on Nginx for 5 minutes",
        alertConditions=[
            AlertCondition(
                Target(
                    expr='sum(irate(nginx_http_requests_total{job="default/frontend",status=~"5.."}[1m]))',
                    legendFormat="5xx",
                    refId='A',
                ),
                timeRange=TimeRange("5m", "now"),
                evaluator=GreaterThan(5),
                operator=OP_AND,
                reducerType=RTYPE_SUM,
            ),
        ],
    )
)

s2 = SingleStat(

    dataSource='prometheus',
    cacheTimeout=None,
    colorBackground=False,
    colorValue=True,
    colors=[
        "rgba(245, 54, 54, 0.9)",
        "rgba(237, 129, 40, 0.89)",
        "rgba(50, 172, 45, 0.97)"
    ],
    decimals=1,
    editable=True,
    # error=False,
    format="s",
    gauge=Gauge(
        maxValue=100,
        minValue=0,
        show=False,
        thresholdLabels=False,
        thresholdMarkers=True
    ),
    height="106px",
    # id=206
    interval=None,
    links=[],
    mappingType=1,
    mappingTypes=[
        {
            "name": "value to text",
            "value": 1
        },
        {
            "name": "range to text",
            "value": 2
        }
    ],
    maxDataPoints=100,
    nullPointMode="connected",
    nullText=None,
    options={},
    postfix="",
    postfixFontSize="50%",
    prefix="",
    prefixFontSize="70%",
    rangeMaps=[
        {
            "from": "null",
            "text": "N/A",
            "to": "null"
        }
    ],
    repeat=None,
    span=4,
    sparkline=SparkLine(
        fillColor=RGBA(31, 118, 189, 0.18),
        full=False,
        lineColor=RGB(31, 120, 193),
        show=False
    ),
    targets=[
        Target(
            expr='process_uptime_seconds{instance="' + instance + '", job="' + job + '"}',
            legendFormat="",
            refId='A',
            step=14400,
            metric="",
            format="time_series",
        )
    ],
    thresholds="",
    title="Uptime",
    valueFontSize="80%",
    valueMaps=[
        {
            "op": "=",
            "text": "N/A",
            "value": "null"
        }
    ],
    valueName="current"
)

dashboard = Dashboard(
    title="HTTP dashboard",
    refresh="5m",
    tags=["python generated dashboard", "dashboard", "spring boot"],
    time=Time('now-15m', 'now'),
    timezone="browser",
    rows=[
        Row(
            title="Quick Facts",
            type="row",
            panels=[
                g1,
                s2
            ]),
        Row(
            title="Quick Facts2",
            type="row",
            panels=[
                g1,
                s2
            ])
    ]
).auto_panel_ids()
