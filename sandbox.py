#$ python3 sandbox.py

import argparse
import asyncio
import pathlib
import os


async def run_behave(args):    
    proc = await asyncio.create_subprocess_exec("behave", *args.split())
    await proc.communicate()

async def main():
    # Get context
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Get opts
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()
    # Set the working directory
    directory_provided = os.path.isdir(args.directory) if args.directory != None else False
    directory = args.directory if directory_provided else current_directory
    # Create a list of test runs
    features = []
    for path in pathlib.Path(directory).rglob('*.feature'):
        args = "--dry-run --junit --quiet --include=" + path.name + ""
        features.append(run_behave(args))
    # Run `behave` so that all .features run at the same time
    await asyncio.gather(*features)
    # ToDo: Handle results
    print("Done!")

# This is the entry point if this file is executed rather than imported
if __name__ == '__main__':
    asyncio.run(main())
