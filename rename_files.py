import argparse
import os
import re

def rename_files():
    args = parse_args()

    if not os.path.isdir(args.folder):
        print('Folder (%s) does not exist' % args.folder)
        return

    print('arguments:')
    print('folder  - "%s"' % args.folder)
    print('pattern - "%s"' % args.pattern)
    print('replace - "%s"' % args.replace)
    print()

    os.chdir(args.folder)
    all_files = next(os.walk(args.folder))[2]

    if not args.regex:
        target_files = [file for file in all_files if args.pattern in file]
    else:
        target_files = {}
        regex = re.compile(args.pattern)
        for file in all_files:
            matched = regex.findall(file)
            if matched:
                target_files[file] = list(set(matched))

    if not target_files:
        print('No files to be renamed')
        return
        
    print('Files to be renamed (%s):' % len(target_files))
    padding = len(max(target_files, key=len))

    replacement_string = args.replace
    for file in target_files:
        if not args.regex:
            if args.append:
                replacement_string = args.pattern + args.replace
            elif args.prepend:
                replacement_string = args.replace + args.pattern

            altered = file.replace(args.pattern, replacement_string)
        else:
            altered = file
            for matched_pattern in target_files[file]:
                if args.append:
                    replacement_string = matched_pattern + args.replace
                elif args.prepend:
                    replacement_string = args.replace + matched_pattern

                altered = file.replace(matched_pattern, replacement_string)

        print('%s --> %s' % (file.ljust(padding), altered))
        if not args.view:
            os.rename(file, altered)

def parse_args():
    parser = argparse.ArgumentParser()

    # Required Args
    parser.add_argument('folder', help='the folder to search through')
    parser.add_argument('pattern', help='the pattern to look for')
    parser.add_argument('replace', help='string to replace the pattern with')

    # Optional Args
    string_location = parser.add_mutually_exclusive_group()
    string_location.add_argument('-a', '--append', action='store_true', help='the "replace" string will be appended to the pattern')
    string_location.add_argument('-p', '--prepend', action='store_true', help='the "replace" string will be prepended to the pattern')
    parser.add_argument('-r', '--regex', action='store_true', help='the pattern is a regex')
    parser.add_argument('-v', '--view', action='store_true', help='only view the potential changes, does not rename files')

    return parser.parse_args()

if __name__ == '__main__':
    rename_files()