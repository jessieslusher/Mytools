def read_first_n_lines(file_path, n, output_file='sample.txt'):
    lines = []
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for _ in range(n):
                line = file.readline().strip()
                if not line:
                    break
                lines.append(line)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return lines
    except Exception as e:
        print(f"An error occurred while reading: {e}")
        return lines

    # Save lines to the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(lines))
        print(f"Lines saved to {output_file.name}")
    except Exception as e:
        print(f"Error saving lines to {output_file.name}: {e}")

    return lines

# Example usage
file_path = 'output.txt'
n = 10000
result_lines = read_first_n_lines(file_path, n)

