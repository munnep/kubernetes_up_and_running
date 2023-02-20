from kubernetes import client, config

# load the default config from $HOME/.kube/config
config.load_kube_config()

v1 = client.CoreV1Api()
log = v1.read_namespaced_pod_log(
  name="nginx-deployment-746ccc65d8-g79j4", namespace="default")

print(log)