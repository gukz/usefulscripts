curl cip.cc | grep 中国 && (
  cat <<EOF | sudo tee /etc/profile.d/pip.sh
export PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
export PIPENV_PYPI_MIRROR=https://mirrors.aliyun.com/pypi/simple/
export PIPENV_VENV_IN_PROJECT=1
EOF
  cat <<EOF | sudo tee /etc/profile.d/npm.sh
export NPM_CONFIG_REGISTRY=https://registry.npm.taobao.org/
export npm_config_registry=https://registry.npm.taobao.org/
EOF
  cat <<EOF | sudo tee /etc/profile.d/goproxy.sh
export GOPROXY=https://goproxy.cn,direct
EOF
  sudo chmod +x /etc/profile.d/pip.sh /etc/profile.d/npm.sh /etc/profile.d/goproxy.sh
)

