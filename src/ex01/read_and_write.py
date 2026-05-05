def convert():
    try:
        with open('ds.csv', 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        with open('ds.tsv', 'w', encoding='utf-8') as f_out:
            for line in lines:
                if not line.strip():
                    f_out.write(line)
                    continue

                new_line = []
                in_quotes = False

                i = 0
                while i < len(line):
                    char = line[i]

                    if char == '"':
                        if i + 1 < len(line) and line[i + 1] == '"':
                            new_line.append('""')
                            i += 1
                        else:
                            in_quotes = not in_quotes
                            new_line.append(char)

                    elif char == ',' and not in_quotes:
                        new_line.append('\t')
                    else:
                        new_line.append(char)

                    i += 1

                f_out.write(''.join(new_line))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    convert()