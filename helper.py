import os
import sys

def create_role_structure(tool_name):
    # Base folder structure for roles
    base_path = f"roles/{tool_name}/"
    paths = {
        'tasks': os.path.join(base_path, 'tasks'),
        'handlers': os.path.join(base_path, 'handlers'),
        'templates': os.path.join(base_path, 'templates'),
        'defaults': os.path.join(base_path, 'defaults'),
        'files': os.path.join(base_path, 'files')
    }

    # Create directories
    for path in paths.values():
        os.makedirs(path, exist_ok=True)

    # Create empty main.yml in tasks
    with open(os.path.join(paths['tasks'], 'main.yml'), 'w') as f:
        pass

    # Create empty OS-specific task files
    for os_name in ['amazon_linux', 'ubuntu', 'centos']:
        with open(os.path.join(paths['tasks'], f'{os_name}.yml'), 'w') as f:
            pass

    # Create empty handlers/main.yml
    with open(os.path.join(paths['handlers'], 'main.yml'), 'w') as f:
        pass

    # Create empty templates/{tool_name}.yml.j2
    with open(os.path.join(paths['templates'], f'{tool_name}.yml.j2'), 'w') as f:
        pass

    # Create empty defaults/main.yml
    with open(os.path.join(paths['defaults'], 'main.yml'), 'w') as f:
        pass

    # Create empty files/{tool_name}.service
    with open(os.path.join(paths['files'], f'{tool_name}.service'), 'w') as f:
        pass

    print(f"Empty role structure for '{tool_name}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_role_structure.py <tool_name>")
    else:
        create_role_structure(sys.argv[1])
