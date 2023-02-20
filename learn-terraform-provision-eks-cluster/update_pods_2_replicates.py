from kubernetes import client, config

# load the default config from $HOME/.kube/config
config.load_kube_config()

v1 = client.AppsV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_namespaced_pod('default')
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# deployment = spec.replicas = 2

api_response = v1.patch_namespaced_deployment(
    name="nginx-deployment",
    namespace="default",
    body={'spec': {'replicas': 2}})