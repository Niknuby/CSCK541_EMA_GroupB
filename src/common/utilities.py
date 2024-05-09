import logging

def configure_logging(log_file, log_format, log_level):
    
    """Configure logging for the application."""
    
    logging.basicConfig(
        filename=log_file,
        format=log_format,
        level=getattr(logging, log_level.upper())
    )

def validate_serialisation_format(format_type):
    
    """Validate if the given serialisation format is supported."""
    
    valid_formats = ['json', 'pickle', 'xml']
    if format_type not in valid_formats:
        raise ValueError(f"Invalid format: {format_type}. Supported formats: {', '.join(valid_formats)}")

def input_with_default(prompt, default_value):
    
    """Prompt user input and return a default value if no input is provided."""
    
    user_input = input(f"{prompt} [{default_value}]: ").strip()
    return user_input or default_value

