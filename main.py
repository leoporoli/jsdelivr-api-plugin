import copy

def create_flow(service_spec, pod_spec, flow_uuid, api_key):
    modified_pod_spec = copy.deepcopy(pod_spec)

    return {
        "pod_spec": modified_pod_spec,
        "config_map": {
        }
    }

def delete_flow(config_map, flow_uuid):
    return
