
#############################################################################################################################
#   filename:reqlibpy.py                                                       
#   created: 2023-02-17                                                              
#   import your librarys below                                                    
#############################################################################################################################
import os
import subprocess
from pkg_resources import working_set, parse_version

REQLIBPY_INITIALIZED = False

def find_requirement_files(root):
    requirement_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.txt'):
                requirement_files.append(os.path.join(dirpath, filename))
    return requirement_files


def install_requirements(requirement_files):
    installed_packages = {pkg.key: pkg.version for pkg in working_set}

    for file_path in requirement_files:
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                if '==' not in line:
                    continue
                package_name, package_version = line.split('==')
                if package_name in installed_packages:
                    installed_version = parse_version(installed_packages[package_name])
                    if parse_version(package_version) > installed_version:
                        try:
                            subprocess.check_call(['pip', 'install', '-U', f"{package_name}=={package_version}"], stderr=subprocess.DEVNULL)
                            print(f"{package_name} atualizado para a versão {package_version}")
                        except subprocess.CalledProcessError:
                            print(f"Erro ao atualizar {package_name} para a versão {package_version}")
                    else:
                        print(f"{package_name} já está instalado na versão {installed_version}")
                else:
                    try:
                        subprocess.check_call(['pip', 'install', f"{package_name}=={package_version}"], stderr=subprocess.DEVNULL)
                        print(f"{package_name} instalado na versão {package_version}")
                    except subprocess.CalledProcessError:
                        print(f"Erro ao instalar {package_name} na versão {package_version}")


def initialize():
    global REQLIBPY_INITIALIZED
    if not REQLIBPY_INITIALIZED:
        project_root = os.getcwd()
        requirement_files = find_requirement_files(project_root)
        if not requirement_files:
            print('Nenhum arquivo de requisitos encontrado na raiz do projeto')
        else:
            install_requirements(requirement_files)
        REQLIBPY_INITIALIZED = True

initialize()
