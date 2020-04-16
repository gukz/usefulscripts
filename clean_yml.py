import fire
import os
import yaml


def walk_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".yml") or name.endswith(".yaml"):
                clean_yaml(name)


def clean_yaml(yaml_file):
    "递归当前目录下所有yaml，移除无效标签"
    remove_meta = ["annotations", "creationTimestamp", "resourceVersion", "selfLink", "uid"]  # noqa
    yamls = []
    with open(yaml_file) as f:
        for y in yaml.safe_load_all(f):
            if y:
                yamls.append(y)
    for yaml_dict in yamls:
        if not yaml_dict:
            continue
        for r_attr in remove_meta:
            if "metadata" in yaml_dict:
                yaml_dict["metadata"].pop(r_attr, None)
    with open(yaml_file, "w") as f:
        yaml.dump_all(yamls, f)


if __name__ == "__main__":
    fire.Fire(walk_files)
