from kubernetes import client, config, watch

# load the default config from $HOME/.kube/config
config.load_kube_config()

v1 = client.CoreV1Api()
w = watch.Watch()

# print(v1.list_namespaced_pod)

for event in w.stream(v1.list_namespaced_pod, "default"):
  print(event.)
