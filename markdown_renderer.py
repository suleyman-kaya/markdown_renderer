import sys

def replace_source_code(markdown_file, *source_code_files):
    try:
        # Markdown dosyasının içeriğini okuyalım
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()

        # Markdown içindeki %%src_code_x%% yerlerini kaynak kodlarıyla değiştirelim
        for i, source_code_file in enumerate(source_code_files, 1):
            placeholder = f'%%src_code_{i}%%'
            with open(source_code_file, 'r') as f:
                source_code_content = f.read()
            markdown_content = markdown_content.replace(placeholder, source_code_content)

        # Yeni markdown içeriğini dosyaya yazalım
        with open('output.md', 'w') as f:
            f.write(markdown_content)

        print("Markdown dosyasının içeriği güncellendi ve 'output.md' olarak kaydedildi.")
    except FileNotFoundError:
        print("Hata: Dosya bulunamadı!")
    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Hata: Markdown dosyası ve en az bir kaynak kod dosyası belirtmelisiniz.")
    else:
        markdown_file = sys.argv[1]
        source_code_files = sys.argv[2:]
        replace_source_code(markdown_file, *source_code_files)
