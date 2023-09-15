Level #7 go to URL and find natas8 user password

- URL: http://natas7.natas.labs.overthewire.org/
- User: natas7
- Password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr 

After navigating to URL an html page with two anchor is rendered, each anchor has an href to an index.html file with a query parameter  
- index.html?page=home
- index.html?page=about  
  
Clicking any of this anchor elements will change the html rendered and the following comment can be found in the developer tools element tab:  
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->  
  
First guess was to pass this suggested path to the php script in the 'page' query parameter value so the backend responds with that resource.  
  
The password for natas8 is a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
