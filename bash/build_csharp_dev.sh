install_mono() {
    sudo apt remove gpg
    sudo apt update
    sudo apt install dirmngr gnupg1 apt-transport-https ca-certificates
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
    sudo sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" > /etc/apt/sources.list.d/mono-official-stable.list'
    sudo apt update
    sudo apt install mono-complete 
}

install_dotnet() {
    wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get update; \
    sudo apt-get install -y apt-transport-https && \
    sudo apt-get update && \
    sudo apt-get install -y dotnet-sdk-3.1
}

option=$1
shift
case "$option" in 
    install_dotnet)
        install_dotnet
        ;;
    install_mono)
        install_mono
        ;;
esac

exit 0
