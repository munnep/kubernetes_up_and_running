import time

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import portforward
import requests


config.load_kube_config()

name_of_pod = 'nginx-deployment-746ccc65d8-g79j4'


pf = portforward(
    core_v1_api.CoreV1Api().connect_get_namespaced_pod_portforward,
    name_of_pod, 'default',
    ports='80',
)
