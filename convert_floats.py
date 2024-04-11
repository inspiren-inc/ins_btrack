import os
import re

def replace_np_float(directory):
    # Compile a regex pattern for 'float' surrounded by word boundaries
    pattern = re.compile(r'\bnp.float\b')
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Use the regex pattern to replace 'float' with 'float'
                modified_content = pattern.sub('float', content)
                
                # Write the modified content back to the file
                with open(file_path, 'w') as f:
                    f.write(modified_content)

# Specify the directory
directory = './'
replace_np_float(directory)
