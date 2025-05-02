import curses

menu = ['Jouer', 'Options', 'Quitter']

def draw_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Définir la hauteur du cadre pour laisser une ligne pour les instructions
    frame_height = h - 2  # On garde une ligne en bas pour les instructions

    # Dessiner une bordure personnalisée (au lieu de stdscr.border()) pour éviter d'écraser la dernière ligne
    stdscr.hline(0, 0, curses.ACS_HLINE, w)
    stdscr.hline(frame_height - 1, 0, curses.ACS_HLINE, w)
    stdscr.vline(0, 0, curses.ACS_VLINE, frame_height)
    stdscr.vline(0, w - 1, curses.ACS_VLINE, frame_height)
    stdscr.addch(0, 0, curses.ACS_ULCORNER)
    stdscr.addch(0, w - 1, curses.ACS_URCORNER)
    stdscr.addch(frame_height - 1, 0, curses.ACS_LLCORNER)
    stdscr.addch(frame_height - 1, w - 1, curses.ACS_LRCORNER)

    # Titre centré
    title = "Bienvenue dans le jeu terminal"
    stdscr.addstr(1, w // 2 - len(title) // 2, title, curses.A_BOLD)

    # Afficher les options du menu
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = frame_height // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    # Ajouter les instructions tout en bas, en dehors du cadre
    instruction = "Utilisez les flèches ↑ ↓ pour naviguer et Entrée pour sélectionner."
    stdscr.addstr(h - 1, w // 2 - len(instruction) // 2, instruction, curses.A_DIM)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    current_row = 0
    draw_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == 'Quitter':
                break
            stdscr.clear()
            stdscr.addstr(0, 0, f"Vous avez sélectionné '{menu[current_row]}'", curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()

        draw_menu(stdscr, current_row)

curses.wrapper(main)
