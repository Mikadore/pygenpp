import click, sh, os, sys
import logging4
from pathlib import Path


logger = logging4.Logger(name="MyLogger")
formatter = '[[time]] - [[name]] - [[level_name]] - [[msg]]'
logger.add_channel(filename=sys.stdout, level=logging4.DEBUG, formatter=formatter)


@click.group()
def cli():
    pass

@click.command()
def init():
    dirpath = os.getcwd()
    assert len(os.listdir(dirpath)) == 0, "Directory must be empty"
    logger.info(f"Initializing directory {dirpath}")
    
        

cli.add_command(init)

if __name__ == "__main__":
    cli()