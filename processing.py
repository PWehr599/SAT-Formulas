import subprocess
import ctypes
import os


def run_all_sat(input_file_path, output_file_path, timeout=120):
    compiled_path = 'minisat/bc_minisat_all_release'
    if not os.path.isfile(compiled_path):
        print(f"File not found: {compiled_path}")
        return False
    if not os.access(compiled_path, os.X_OK):
        print(f"File is not executable: {compiled_path}")
        return False

    try:
        result = subprocess.run(
            [f"./{compiled_path}", input_file_path, output_file_path],
            timeout=timeout,
            check=True
        )
        return True

    except subprocess.TimeoutExpired:
        print(f"The process timed out after {timeout} seconds.")
    except subprocess.CalledProcessError as e:
        print(f"The process failed with exit code {e.returncode}.")
    except OSError as e:
        print(f"OSError: {e}")

    return False
