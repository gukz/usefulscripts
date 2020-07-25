import fire
import os
import yaml


def walk_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for name in files:
            if name.endswith(".yml") or name.endswith(".yaml"):
                clean_yaml(os.path.join(root, name))


def clean_dict(d):
    remove = [
        "annotations",
        "strategy",
        "progressDeadlineSeconds",
        "revisionHistoryLimit",
        "terminationMessagePath",
        "terminationMessagePolicy",
        "dnsPolicy",
        "restartPolicy",
        "schedulerName",
        "securityContext",
        "terminationGracePeriodSeconds",
        "creationTimestamp",
        "resourceVersion",
        "selfLink",
        "uid",
        "status",
        "generation",
    ]  # noqa
    if "image" in d:
        d["image"] = "{{IMAGE}}"
    for r in remove:
        d.pop(r, None)
    for _, v in d.items():
        if type(v) == dict:
            clean_dict(v)


def clean_yaml(yaml_file):
    "递归当前目录下所有yaml，移除无效标签"
    yamls = []
    with open(yaml_file) as f:
        for y in yaml.safe_load_all(f):
            if y:
                yamls.append(y)
    for yaml_dict in yamls:
        if not yaml_dict:
            continue
        yaml_dict["apiVersion"] = "apps/v1"
        clean_dict(yaml_dict)
    with open(yaml_file, "w") as f:
        yaml.dump_all(yamls, f)


if __name__ == "__main__":
    fire.Fire(walk_files)
