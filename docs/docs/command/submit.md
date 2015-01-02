#Submit

This command is useful for submitting problem to spoj. By running `spoj submit --help` you will see the similar output:

```
Usage: spoj submit [OPTIONS] FILENAME

Options:
  -p, --problem TEXT              Problem code
  -l, --language [1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|38|39|41|42|46|54|56|62|98|99|104|111|114|116|124|126]
                                  Language of problem. See `spoj
                                  language`
  --help                          Show this message and exit.
```

* Required Arguments
    * **FILENAME**  
        Specify the path of the file you want to submit. Make sure this file is readable and exists. If this file 
        doesn't exist then you will get similar error message  
        
        
            Error: Invalid value for "filename": Could not open file: <FILENAME>: 
            No such file or directory
        

* Optional Arguments
    * **-p, --problem TEXT**  
        Specify the problem code for you want to submit the solution.  
        If this argument is not present then the filename will be considered as problem code.
        
        
            Example:
            filename: ~/username/spoj/myfile.py
            problem name used: MYFILE
            
            filename: /path/to/someFile
            problem name used: SOMEFILE
    
    * **-l, --language**
        Specify the language code for the problem you are submitting. If this field is not present then the 
        language is taken from configuration file if already configured. If the language is not configured then 
        A prompt will ask for language code.
        
        See [`spoj language`](language) for supported language and codes
       
        