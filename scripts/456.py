import hou
import sys

def add_path_to_site_packages(additional_path):
    full_additional_path = hou.text.expandString(additional_path)

    # Clean up path
    if not hasattr(hou.session, "venv_site_packages_path"):
        setattr(hou.session, "venv_site_packages_path", "")
    sys.path = list(filter(lambda path: path != full_additional_path, sys.path))

    # Set venv site-packages path
    hou.session.venv_site_packages_path = full_additional_path
    sys.path.append(full_additional_path)
    # print("append venv site-packages: " + full_additional_path)

def load_venv_site_packages():
	additional_packages = []
	additional_packages.append("$JOB/.venv/Lib/site-packages")
	raw_env_paths = hou.getenv("ADDITIONAL_SITE_PACKAGES")
	if raw_env_paths is not None:
		additional_packages.append(hou.getenv("ADDITIONAL_SITE_PACKAGES", default_value="").split(';'))
	for path in additional_packages:
		add_path_to_site_packages(path)

load_venv_site_packages()