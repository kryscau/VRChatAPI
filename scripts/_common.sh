#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

app="vrchat-api"
domain=$YNH_APP_ARG_DOMAIN
final_path="/var/www/$app"

#=================================================
# GENERIC HELPERS
#=================================================

ynh_print_info() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $app: $1"
}

ynh_die() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $app [ERR]: $1" >&2
    exit 1
}

#=================================================
# SPECIFIC HELPERS
#=================================================

ynh_virtualenv_setup() {
    ynh_print_info "Creating virtual environment for $app"
    python3 -m venv "$final_path/venv" || ynh_die "Failed to create virtualenv"
    source "$final_path/venv/bin/activate"
    pip install --upgrade pip setuptools wheel
    pip install -r "$final_path/requirements.txt" || ynh_die "Failed to install Python dependencies"
}
