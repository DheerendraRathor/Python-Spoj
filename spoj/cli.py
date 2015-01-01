import click
import lang
import utils
import config as Config
from spoj import Spoj
import multiprocessing

@click.group()
@click.version_option()
@click.pass_context
def main(ctx):
    pass


@click.command()
@click.argument('filename', required=True, type=click.File())
@click.option('--problem', '-p', help='Problem code')
@click.option('--language', '-l', help='Language of problem. \033[91mSee `spoj language`\033[0m',
              type=click.Choice(map(str, sorted([lan[0] for lan in lang.LANG]))))
def submit(filename, problem, language):
    if problem is None:
        name = filename.name
        name = name.split('/')[-1]
        try:
            name = name.split('.')[-2]
        except Exception:
            name = name.split('.')[-1]
        problem = name.upper()
    spoj = Spoj(problem,language,filename)
    submit_status, message = spoj.submit()
    if submit_status:
        print message
        spoj.fetch_status()
    else:
        print message


@click.command()
@click.option('--language', '-l', help='Choose Default Language. \033[91mSee `spoj language`\033[0m',
              type=click.Choice(map(str, sorted([lan[0] for lan in lang.LANG]))))
@click.option('--credential', '-c', is_flag=True)
@click.pass_context
def config(ctx, language, credential):
    if credential:
        username, password = utils.ask_credentials()
        click.echo('Verifying Credentials...Please wait')
        creds = Spoj.verify_credentials(username, password)
        if not creds:
            ctx.exit()
        Config.set_credentials(username, password)
    if language is not None:
        Config.set_language(language)
    pass


@click.command()
def language():
    click.echo_via_pager('Supported Languages:\n' +
                             '\n'.join('\t\033[94m%s\033[0m : \033[91m%d\033[0m' % (lan[1], lan[0])
                                       for lan in lang.LANG))

@click.command()
def status():
    pass


main.add_command(submit)
main.add_command(config)
main.add_command(language)
main.add_command(status)