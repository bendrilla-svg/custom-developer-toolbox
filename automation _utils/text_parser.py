def extract_log_keywords(file_path, keyword):
    """Scans structural files or logs to extract key actionable data lines."""
    matched_lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if keyword.lower() in line.lower():
                    matched_lines.append(f"Line {line_num}: {line.strip()}")
        return matched_lines
    except FileNotFoundError:
        return [f"Error: File {file_path} not found."]

if __name__ == "__main__":
    # Example usage for log extraction pipelines
    print("Log parsing utility operational.")
