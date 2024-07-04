import os
import subprocess
import sys
import venv

def create_virtual_env(env_dir):
    """Create a virtual environment."""
    venv.create(env_dir, with_pip=True)
    print(f"Virtual environment created at {env_dir}")

def install_requirements(env_dir, requirements_file):
    """Install requirements using pip."""
    pip_executable = os.path.join(env_dir, 'bin', 'pip') if os.name != 'nt' else os.path.join(env_dir, 'Scripts', 'pip.exe')
    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
    print(f"Requirements from {requirements_file} installed")

def run_in_virtual_env(env_dir, command):
    """Run a command in the virtual environment."""
    python_executable = os.path.join(env_dir, 'bin', 'python') if os.name != 'nt' else os.path.join(env_dir, 'Scripts', 'python.exe')
    env = os.environ.copy()
    env['VIRTUAL_ENV'] = env_dir
    env['PATH'] = os.path.join(env_dir, 'bin') + os.pathsep + env['PATH'] if os.name != 'nt' else os.path.join(env_dir, 'Scripts') + os.pathsep + env['PATH']
    
    subprocess.check_call([python_executable, '-m', 'pip', 'install', '--upgrade', 'pip'], env=env)  # Upgrade pip in the virtual environment
    subprocess.check_call([python_executable] + command, env=env)

def main():
    env_dir = 'env'
    requirements_file = 'requirements.txt'
    
    # Check if requirements file exists
    if not os.path.isfile(requirements_file):
        print(f"{requirements_file} not found.")
        sys.exit(1)

    # Create the virtual environment
    create_virtual_env(env_dir)
    
    # Install the requirements
    install_requirements(env_dir, requirements_file)

    # Run a command in the virtual environment (example: print Python version)
    run_in_virtual_env(env_dir, ['-c', 'import sys; print("Python version:", sys.version)'])

if __name__ == "__main__":
    main()
