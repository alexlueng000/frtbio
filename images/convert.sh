for file in *.jpg; do cwebp -q 60 "$file" -o "${file%.jpg}.webp"; done
