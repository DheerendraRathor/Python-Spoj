#Configuration

If you want to avoid entering credentials for every submit or want to setup your favourite language, it is advised to
properly configure after installation.

To see help about configuration use `spoj config --help`. This will display following screen

```
Usage: spoj config [OPTIONS]

Options:
  -l, --language [1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|38|39|41|42|46|54|56|62|98|99|104|111|114|116|124|126]
                                  Choose Default Language. See `spoj
                                  language`
  -c, --credential
  --help                          Show this message and exit.
```

##Credentials

To store your credentials use `spoj config -c/--credential`. After running this command, few prompt will appear

* `Username: ` - Enter your SPOJ username here
* `Password: ` - Enter your SPOJ password here
* `Confirm Password: ` - Enter your SPOJ password again for confirmation.

After these three prompts, your password will be verified with SPOJ server and after verification your credentials will be remembered and will not be asked again while submitting.

> Your credentials are stored on your PC in a configuration file. We **do not** save or store your credentials on any server on internet.

##Language

To mark your favourite programming language, use `spoj config -l/--language <language code>`.
The language code should be an integer and should be available in the list produced by `spoj language`.
For details see command [`spoj language`](language).