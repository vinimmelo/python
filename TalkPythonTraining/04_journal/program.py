import journal


def main():
    print_header()
    run_event_loop()


def print_header() :
    print('-----------------------------------')
    print('           BIRTHDAY APP')
    print('-----------------------------------')


def run_event_loop() :
    print('What you want to do with your journal?')

    cmd = "EMPTY"

    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'X' and cmd:
        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ')
        cmd = cmd.upper().strip()

        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entries(journal_data)
        elif cmd != 'X':
            print('Choose something brow')

    print('Done, goodbye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your entries in the journal:')
    for ind, entry in enumerate(data):
        print(f'[{ind + 1}] - {entry.rstrip()}')


def add_entries(data):
    entry = input('Digit your entry to the journal, press <enter> to exit: ')
    data.append(entry)


if __name__ == '__main__':
    main()
