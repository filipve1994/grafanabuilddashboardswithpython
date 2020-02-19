from src.core import *
from src.prometheus import *

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
    # gauge={
    #     #     "maxValue": 100,
    #     #     "minValue": 0,
    #     #     "show": False,
    #     #     "thresholdLabels": False,
    #     #     "thresholdMarkers": True
    #     # },
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
    # sparkline={
    #     "fillColor": "rgba(31, 118, 189, 0.18)",
    #     "full": False,
    #     "lineColor": "rgb(31, 120, 193)",
    #     "show": False
    # },
    sparkline=SparkLine(
        # fillColor="rgba(31, 118, 189, 0.18)",
        fillColor=RGBA(31, 118, 189, 0.18),
        full=False,
        # lineColor="rgb(31, 120, 193)",
        lineColor=RGB(31, 120, 193),
        show=False
    ),
    targets=[
        Target(
            expr='process_uptime_seconds{instance="arte2-cp11-lp.msnet.railb.be:15881", job="upmviziworks-backend-application"}',
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
    rows=[
        Row(
            title="Row title test",
            panels=[
            g1,
            s2
        ])
    ]
).auto_panel_ids()
