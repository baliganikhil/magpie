#!/usr/bin/env bash

nvm_check() {
    # touch ~/.bashrc
    # touch ~/.bash_profile

    source ~/.bashrc
    source ~/.bash_profile

    echo
    echo Checking if nvm exists...
    if [ "$(nvm --version)" ]; then
        echo nvm \(ver: $(nvm --version)\) exists... Skipping installation
    else
        echo nvm does not exist... Installing
        # curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
    fi
}

node_install() {

}