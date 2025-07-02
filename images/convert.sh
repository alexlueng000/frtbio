for file in *.png; do cwebp -q 60 "$file" -o "${file%.png}.webp"; done
