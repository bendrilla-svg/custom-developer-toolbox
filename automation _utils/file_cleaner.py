import os
import shutil

def clear_temp_files(directory_path):
    """Automates system housekeeping by clearing specified temporary file paths."""
    if not os.path.exists(directory_path):
        print(f"Path {directory_path} does not exist.")
        return
        
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f"Successfully cleared: {filename}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == "__main__":
    # Example directory path to clean up workspace bloat
    target_dir = "./sandbox_temp"
    print(f"Initializing automated clean-up for {target_dir}...")
