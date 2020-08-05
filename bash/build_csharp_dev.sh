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
    mkdir /csharp_runtime
    cd /csharp_runtime
    wget https://download.visualstudio.microsoft.com/download/pr/9eadec7a-dd7e-476d-a348-c4bf946a0bad/c11b5123931ee17faba27e5debe74731/aspnetcore-runtime-3.1.6-linux-x64.tar.gz
    mkdir aspnetcore-runtime-3.1.6-linux-x64
    tar -zxvf aspnetcore-runtime-3.1.6-linux-x64.tar.gz -C /csharp_runtime/aspnetcore-runtime-3.1.6-linux-x64
    sudo rm /usr/local/bin/dotnet
    sudo ln -sf /csharp_runtime/aspnetcore-runtime-3.1.6-linux-x64/dotnet /usr/local/bin
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
