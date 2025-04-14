import curses

COLOR_DIM = 1
COLOR_WHITE_ON_BLUE = 2

def multi_choice_input(stdscr, question, options):
    current_option = 0

    def print_menu(stdscr, question, options):
        curses.curs_set(0)
        stdscr.clear()

        curses.init_pair(COLOR_WHITE_ON_BLUE, curses.COLOR_BLACK, curses.COLOR_BLUE)
        curses.init_pair(COLOR_DIM, curses.A_DIM, curses.A_INVIS)
        stdscr.addstr(0, 0, question, curses.color_pair(COLOR_DIM))

        for index, option in enumerate(options):
            x = 0
            y = index + 1
            if(index == current_option):
                stdscr.addstr(y, x, option, curses.color_pair(COLOR_WHITE_ON_BLUE))
            else:
                stdscr.addstr(y, x, option)
                pass
        stdscr.refresh()

    while True:
        print_menu(stdscr, question, options)
        key = stdscr.getch()

        if(key == curses.KEY_UP and current_option > 0 ):
            current_option -= 1

        elif(key == curses.KEY_DOWN and current_option < len(options) - 1 ):
            current_option += 1
        
        elif(key == curses.KEY_ENTER or key == 10):
            return current_option
        
        elif(key == 27):
            return None